# aaudiototext

Transcribes audio and video files locally on Apple Silicon using MLX Whisper, then summarizes them with a local LLM via Ollama. Everything runs on-device -- no cloud services or accounts needed.

## What it does

1. Takes an audio or video file as input
2. Converts video to mp3 (320kbps) via ffmpeg if needed
3. Transcribes using MLX Whisper, hardware-accelerated on Apple Silicon GPU
4. Sends the transcript to `qwen3.5:9b` via Ollama for summarization
5. Saves output to `~/Downloads/Transcriptions/<filename>/` and opens the folder

Each run produces two files:
- `timestamps.txt` -- full transcript with `[HH:MM:SS.mmm]` timestamps
- `summary.md` -- structured summary with key points, decisions, and action items

## Requirements

- macOS with Apple Silicon (M1/M2/M3/M4)
- Python 3.9+
- [ffmpeg](https://ffmpeg.org/) (for video conversion and duration detection)
- [Ollama](https://ollama.com/) with `qwen3.5:9b` pulled
- Python package: `mlx-whisper`

Pull the summarization model:

```bash
ollama pull qwen3.5:9b
```

Install the Python dependency:

```bash
pip install mlx-whisper
```

## Usage

**Full pipeline** (transcribe + summarize):

```bash
python .venv/main.py /path/to/recording.mp4
python .venv/main.py /path/to/meeting.m4a
```

**Pick a Whisper model size** (defaults to `large-v3`):

```bash
python .venv/main.py --model small /path/to/recording.mp4
```

Available models: `tiny`, `base`, `small`, `medium`, `large`, `large-v2`, `large-v3`

**Summarize only** (re-run summary on an existing transcription):

```bash
python .venv/main.py --summarize ~/Downloads/Transcriptions/<folder>/timestamps.txt
```

## Supported formats

| Type  | Extensions                                              |
|-------|---------------------------------------------------------|
| Audio | `.mp3`, `.wav`, `.m4a`, `.flac`, `.ogg`, `.aac`        |
| Video | `.mp4`, `.mov`, `.avi`, `.mkv`, `.webm`, `.m4v`, `.wmv`, `.flv` |

## Notes

- Ollama starts automatically if it is not running and stops after the summary is done
- MLX Whisper models are downloaded from HuggingFace on first use (large-v3 is roughly 3 GB)
- At the end of each run, you get a "time saved" comparison between media length and processing time
