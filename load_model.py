from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

# Load the tokenizer and model
tokenizer = LlamaTokenizer.from_pretrained("path_to_llama_model")
model = LlamaForCausalLM.from_pretrained("path_to_llama_model").to("cuda")