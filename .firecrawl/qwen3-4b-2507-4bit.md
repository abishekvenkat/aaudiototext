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

# [![](https://cdn-avatars.huggingface.co/v1/production/uploads/623c830997ddced06d78699b/3qTjC7d3YFCJTwpxd2noq.png)](https://huggingface.co/mlx-community)  [mlx-community](https://huggingface.co/mlx-community)  /      [Qwen3-4B-Instruct-2507-4bit](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit)    like9           Follow ![](https://cdn-avatars.huggingface.co/v1/production/uploads/623c830997ddced06d78699b/3qTjC7d3YFCJTwpxd2noq.png)MLX Community10.9k

[Text Generation](https://huggingface.co/models?pipeline_tag=text-generation) [MLX](https://huggingface.co/models?library=mlx) [Safetensors](https://huggingface.co/models?library=safetensors) [qwen3](https://huggingface.co/models?other=qwen3) [conversational](https://huggingface.co/models?other=conversational) [4-bit precision](https://huggingface.co/models?other=4-bit)

License:apache-2.0

[Model card](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit) [FilesFiles and versions\\
xet](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit/tree/main) [Community\\
1](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit/discussions)

Use this model

- [mlx-community/Qwen3-4B-Instruct-2507-4bit](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit#mlx-communityqwen3-4b-instruct-2507-4bit "mlx-community/Qwen3-4B-Instruct-2507-4bit")
  - [Use with mlx](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit#use-with-mlx "Use with mlx")

# mlx-community/Qwen3-4B-Instruct-2507-4bit

This model [mlx-community/Qwen3-4B-Instruct-2507-4bit](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit) was
converted to MLX format from [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)
using mlx-lm version **0.26.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Qwen3-4B-Instruct-2507-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```

Downloads last month42,394

Safetensors

Model size

0.6B params

Tensor type

BF16

·

U32

·

Chat template

Files info

MLX

Hardware compatibility

[Log In](https://huggingface.co/login?next=https%3A%2F%2Fhuggingface.co%2Fmlx-community%2FQwen3-4B-Instruct-2507-4bit) to add your hardware

4-bit

MLX

2.26 GB

Inference Providers [NEW](https://huggingface.co/docs/inference-providers)

[Text Generation](https://huggingface.co/tasks/text-generation "Learn more about text-generation")

This model isn't deployed by any Inference Provider. [🙋Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=mlx-community/Qwen3-4B-Instruct-2507-4bit&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5Bmlx-community%2FQwen3-4B-Instruct-2507-4bit%5D(%2Fmlx-community%2FQwen3-4B-Instruct-2507-4bit)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A(optional)%20Which%20providers%20are%20you%20interested%20in%3F%20(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6)%0A)

## Model tree for mlx-community/Qwen3-4B-Instruct-2507-4bit

Base model

[Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)

Quantized

( [227](https://huggingface.co/models?other=base_model:quantized:Qwen/Qwen3-4B-Instruct-2507))

this model

Adapters

[1 model](https://huggingface.co/models?other=base_model:adapter:mlx-community/Qwen3-4B-Instruct-2507-4bit)

Finetunes

[1 model](https://huggingface.co/models?other=base_model:finetune:mlx-community/Qwen3-4B-Instruct-2507-4bit)

System theme

Company

[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/)  [Hugging Face](https://huggingface.co/)

Website

[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

Inference providers allow you to run inference using different serverless providers.

StripeM-Inner