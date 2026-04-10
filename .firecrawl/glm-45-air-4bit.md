[![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)Hugging Face](https://huggingface.co/)

- [Models](https://huggingface.co/models)
- [Datasets](https://huggingface.co/datasets)
- [Spaces](https://huggingface.co/spaces)
- [Buckets new](https://huggingface.co/storage)
- [Docs](https://huggingface.co/docs)
- [Enterprise](https://huggingface.co/enterprise)
- [Pricing](https://huggingface.co/pricing)

- * * *

- [Log In](https://huggingface.co/login)
- [Sign Up](https://huggingface.co/join)

# [![](https://cdn-avatars.huggingface.co/v1/production/uploads/623c830997ddced06d78699b/3qTjC7d3YFCJTwpxd2noq.png)](https://huggingface.co/mlx-community)  [mlx-community](https://huggingface.co/mlx-community)  /      [GLM-4.5-Air-4bit](https://huggingface.co/mlx-community/GLM-4.5-Air-4bit)    like27           Follow ![](https://cdn-avatars.huggingface.co/v1/production/uploads/623c830997ddced06d78699b/3qTjC7d3YFCJTwpxd2noq.png)MLX Community10.9k

[Text Generation](https://huggingface.co/models?pipeline_tag=text-generation) [MLX](https://huggingface.co/models?library=mlx) [Safetensors](https://huggingface.co/models?library=safetensors) [English](https://huggingface.co/models?language=en) [Chinese](https://huggingface.co/models?language=zh) [glm4\_moe](https://huggingface.co/models?other=glm4_moe) [conversational](https://huggingface.co/models?other=conversational) [4-bit precision](https://huggingface.co/models?other=4-bit)

License:mit

[Model card](https://huggingface.co/mlx-community/GLM-4.5-Air-4bit) [FilesFiles and versions\\
xet](https://huggingface.co/mlx-community/GLM-4.5-Air-4bit/tree/main) [Community\\
1](https://huggingface.co/mlx-community/GLM-4.5-Air-4bit/discussions)

Use this model

- [mlx-community/GLM-4.5-Air-4bit](https://huggingface.co/mlx-community/GLM-4.5-Air-4bit#mlx-communityglm-45-air-4bit "mlx-community/GLM-4.5-Air-4bit")
  - [Use with mlx](https://huggingface.co/mlx-community/GLM-4.5-Air-4bit#use-with-mlx "Use with mlx")

# mlx-community/GLM-4.5-Air-4bit

This model [mlx-community/GLM-4.5-Air-4bit](https://huggingface.co/mlx-community/GLM-4.5-Air-4bit) was
converted to MLX format from [zai-org/GLM-4.5-Air](https://huggingface.co/zai-org/GLM-4.5-Air)
using mlx-lm version **0.26.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/GLM-4.5-Air-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```

Downloads last month244

MLX

Hardware compatibility

[Log In](https://huggingface.co/login?next=https%3A%2F%2Fhuggingface.co%2Fmlx-community%2FGLM-4.5-Air-4bit) to add your hardware

4-bit

MLX

60.1 GB

Inference Providers [NEW](https://huggingface.co/docs/inference-providers)

[Text Generation](https://huggingface.co/tasks/text-generation "Learn more about text-generation")

This model isn't deployed by any Inference Provider. [🙋1Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/3721)

## Model tree for mlx-community/GLM-4.5-Air-4bit

Base model

[zai-org/GLM-4.5-Air](https://huggingface.co/zai-org/GLM-4.5-Air)

Quantized

( [60](https://huggingface.co/models?other=base_model:quantized:zai-org/GLM-4.5-Air))

this model

Quantizations

[Use with llama.cpp](https://huggingface.co/models?apps=llama.cpp&other=base_model:quantized:mlx-community/GLM-4.5-Air-4bit "Use with llama.cpp")[Use with LM Studio](https://huggingface.co/models?apps=lmstudio&other=base_model:quantized:mlx-community/GLM-4.5-Air-4bit "Use with LM Studio")[Use with Jan](https://huggingface.co/models?apps=jan&other=base_model:quantized:mlx-community/GLM-4.5-Air-4bit "Use with Jan")[Use with Ollama](https://huggingface.co/models?apps=ollama&other=base_model:quantized:mlx-community/GLM-4.5-Air-4bit "Use with Ollama")

[1 model](https://huggingface.co/models?other=base_model:quantized:mlx-community/GLM-4.5-Air-4bit)

## Collections including mlx-community/GLM-4.5-Air-4bit

[**GLM 4.5**\\
\\
Collection\\
\\
2 items•Updated Jul 28, 2025• 7](https://huggingface.co/collections/mlx-community/glm-45)

[**GLM-4.5-Air**\\
\\
Collection\\
\\
4 items•Updated Oct 1, 2025• 1](https://huggingface.co/collections/mlx-community/glm-45-air)

System theme

Company

[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/)  [Hugging Face](https://huggingface.co/)

Website

[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

Inference providers allow you to run inference using different serverless providers.