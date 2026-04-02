import os
import mlx_whisper
import datetime
import subprocess
import json
import sys
import tempfile
import time
import urllib.request

# ── Config ───────────────────────────────────────────────────────────────────
OUTPUT_BASE = "/Users/abishekvenkat/Downloads/Transcriptions"
OLLAMA_MODEL = "qwen3.5:9b"
OLLAMA_URL = "http://localhost:11434/api/generate"

VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v", ".wmv", ".flv"}
AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".flac", ".ogg", ".aac"}

# MLX uses HuggingFace repos instead of built-in models
MLX_MODELS = {
    "tiny": "mlx-community/whisper-tiny-mlx",
    "base": "mlx-community/whisper-base-mlx",
    "small": "mlx-community/whisper-small-mlx",
    "medium": "mlx-community/whisper-medium-mlx",
    "large": "mlx-community/whisper-large-mlx",
    "large-v2": "mlx-community/whisper-large-v2-mlx",
    "large-v3": "mlx-community/whisper-large-v3-mlx"
}


def get_duration(path):
    """Return media duration in seconds using ffprobe."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path],
        capture_output=True, text=True
    )
    try:
        return float(result.stdout.strip())
    except ValueError:
        return None


def format_timestamp(seconds):
    td = datetime.timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    milliseconds = int(td.microseconds / 1000)
    return f"[{hours:02}:{minutes:02}:{secs:02}.{milliseconds:03}]"


def convert_video_to_audio(video_path):
    """Convert video to mp3 at 320kbps using ffmpeg, returns temp file path."""
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tmp.close()
    print("Converting video to audio...")
    subprocess.run(
        ["ffmpeg", "-y", "-i", video_path, "-b:a", "320k", "-map", "a", tmp.name],
        check=True, capture_output=True,
    )
    return tmp.name


def ollama_is_running():
    try:
        urllib.request.urlopen("http://localhost:11434", timeout=2)
        return True
    except Exception:
        return False


def start_ollama():
    """Start ollama serve in the background, return the process."""
    print("Starting ollama...")
    proc = subprocess.Popen(
        ["ollama", "serve"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    for _ in range(20):
        time.sleep(0.5)
        if ollama_is_running():
            print("Ollama started.")
            return proc
    print("[!] Ollama did not start in time.")
    proc.terminate()
    return None


def generate_summary(transcription_text):
    """Send transcription to local ollama model and return the summary markdown."""
    we_started_ollama = False
    ollama_proc = None

    if not ollama_is_running():
        ollama_proc = start_ollama()
        if ollama_proc is None:
            return None
        we_started_ollama = True

    prompt = (
            "You are an expert at extracting meaningful information from meeting transcripts. "
            "Read the transcript below carefully and produce a detailed, specific summary. "
            "Do not generalize or paraphrase vaguely — use the actual words, names, topics, and examples from the transcript.\n\n"
            "Respond with exactly these sections:\n\n"
            "## Summary\n"
            "2-4 sentences covering what the meeting was about, who was involved (if mentioned), and what was accomplished.\n\n"
            "## Key Discussion Points\n"
            "A bulleted list of the main topics discussed. Each bullet should be specific — avoid generic statements like 'the team discussed challenges'. Say what the challenge actually was.\n\n"
            "## Decisions Made\n"
            "A bulleted list of concrete decisions or conclusions reached. If none were made, say so explicitly.\n\n"
            "## Action Items\n"
            "A bulleted list of tasks, follow-ups, or next steps. Include the owner and deadline if mentioned. If none were stated, say so explicitly.\n\n"
            "Transcript:\n\n"
            + transcription_text
    )
    payload = json.dumps({
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "think": False
    }).encode()
    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    result = None
    try:
        with urllib.request.urlopen(req, timeout=1800) as resp:
            data = json.loads(resp.read())
            result = data.get("response", "").strip()
    except urllib.error.URLError as e:
        print(f"\n[!] Ollama request failed: {e}")

    if we_started_ollama and ollama_proc:
        print("Stopping ollama...")
        ollama_proc.terminate()
        ollama_proc.wait()

    return result


def fmt_duration(seconds):
    h, r = divmod(int(seconds), 3600)
    m, s = divmod(r, 60)
    if h:
        return f"{h}h {m}m {s}s"
    if m:
        return f"{m}m {s}s"
    return f"{s}s"


def summarize_only(timestamps_path):
    """Run just the summary step on an existing timestamps.txt."""
    if not os.path.exists(timestamps_path):
        print(f"[!] File not found: {timestamps_path}")
        sys.exit(1)

    out_dir = os.path.dirname(os.path.abspath(timestamps_path))
    print(f"Summarizing existing transcription: {timestamps_path}")

    with open(timestamps_path, encoding="utf-8") as f:
        transcription_text = f.read()

    print(f"Generating summary with {OLLAMA_MODEL}...")
    t0 = time.time()
    summary = generate_summary(transcription_text)
    elapsed = time.time() - t0

    summary_path = os.path.join(out_dir, "summary.md")
    if summary:
        folder_name = os.path.basename(out_dir)
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(f"# {folder_name}\n\n")
            f.write(summary)
        print(f"\nSummary saved: {summary_path}  ({fmt_duration(elapsed)})")
    else:
        print("[!] Summary generation failed.")
        sys.exit(1)

    subprocess.run(["open", out_dir])


def main():
    import argparse
    parser = argparse.ArgumentParser(prog="main.py")
    parser.add_argument("input", nargs="?", help="Audio or video file to transcribe")
    parser.add_argument("--model", default="large-v3", choices=list(MLX_MODELS.keys()),
                        help="Whisper model to use (default: large-v3)")
    parser.add_argument("--summarize", metavar="TIMESTAMPS_FILE",
                        help="Run summary only on an existing timestamps.txt")
    args = parser.parse_args()

    if args.summarize:
        summarize_only(args.summarize)
        return

    if not args.input:
        parser.print_help()
        sys.exit(1)

    input_path = args.input
    if not os.path.exists(input_path):
        print(f"[!] File not found: {input_path}")
        sys.exit(1)

    ext = os.path.splitext(input_path)[1].lower()
    tmp_audio = None

    if ext in VIDEO_EXTS:
        tmp_audio = convert_video_to_audio(input_path)
        audio_path = tmp_audio
    elif ext in AUDIO_EXTS:
        audio_path = input_path
    else:
        print(f"[!] Unsupported file type: {ext}")
        sys.exit(1)

    media_duration = get_duration(audio_path)
    if media_duration is None:
        print("[!] Could not determine media duration via ffprobe.")
        sys.exit(1)

    print(f"File:     {os.path.basename(input_path)}")
    print(f"Duration: {fmt_duration(media_duration)}")

    # ── Transcribe natively on Apple Silicon using MLX ──
    t0 = time.time()
    hf_repo = MLX_MODELS[args.model]
    print(f"\n⚡ Transcribing via Apple MLX ({hf_repo}) on M3 Pro GPU...")
    print("-" * 52)

    # This automatically downloads the optimized MLX weights on the first run
    result = mlx_whisper.transcribe(
        audio_path,
        path_or_hf_repo=hf_repo,
        verbose=True  # Streams output directly to terminal
    )

    print("-" * 52)
    transcribe_time = time.time() - t0

    if tmp_audio:
        os.unlink(tmp_audio)

    # Create output folder
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    out_dir = os.path.join(OUTPUT_BASE, base_name)
    os.makedirs(out_dir, exist_ok=True)

    # Save timestamped transcription
    timestamps_path = os.path.join(out_dir, "timestamps.txt")
    with open(timestamps_path, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            start = format_timestamp(segment["start"])
            end = format_timestamp(segment["end"])
            text = segment["text"].strip()
            f.write(f"{start} --> {end}: {text}\n")

    # Generate summary via ollama
    print(f"\nGenerating summary with {OLLAMA_MODEL}...")
    t1 = time.time()
    with open(timestamps_path, encoding="utf-8") as f:
        transcription_text = f.read()

    summary = generate_summary(transcription_text)
    summary_time = time.time() - t1

    summary_path = os.path.join(out_dir, "summary.md")
    if summary:
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(f"# {base_name}\n\n")
            f.write(summary)

    # Time saved
    total_processing = transcribe_time + summary_time
    time_saved_pct = max(0.0, (media_duration - total_processing) / media_duration * 100)

    # Summary output
    print()
    print("=" * 52)
    print(f"  Transcription: {timestamps_path}")
    if summary:
        print(f"  Summary:       {summary_path}")
    else:
        print("  Summary:       skipped (see ollama error above)")
    print()
    print(f"  Media length:  {fmt_duration(media_duration)}")
    print(f"  Processed in:  {fmt_duration(total_processing)}")
    print(f"  Time saved:    {time_saved_pct:.0f}%")
    if time_saved_pct >= 50:
        print(f"  Congrats! You saved {time_saved_pct:.0f}% of your time!")
    print("=" * 52)

    subprocess.run(["open", out_dir])


if __name__ == "__main__":
    main()