import os
from huggingface_hub import hf_hub_download

def main():
    print("Downloading GPT-2 (124M) ONNX model...")
    # Xenova/gpt2 contains pre-exported ONNX weights for GPT-2 
    # which is perfect for plugging straight into the MAX engine.
    
    os.makedirs("models/gpt2", exist_ok=True)
    
    model_path = hf_hub_download(
        repo_id="Xenova/gpt2",
        filename="onnx/decoder_model.onnx",
        local_dir="models/gpt2"
    )
    
    print(f"Successfully downloaded GPT-2 ONNX model to: {model_path}")

if __name__ == "__main__":
    main()
