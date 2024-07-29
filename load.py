import os
import requests
from tqdm import tqdm

LLAMA_MODEL_URL = "https://huggingface.co/IlyaGusev/saiga2_7b_gguf/resolve/main/model-q2_K.gguf"
LLAMA_MODEL_PATH = "model-q2_K.gguf"

def download_model():
    if os.path.exists(LLAMA_MODEL_PATH):
        print(f"Model already exists at {LLAMA_MODEL_PATH}. Skipping download.")
        return
    
    response = requests.get(LLAMA_MODEL_URL, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))

    with open(LLAMA_MODEL_PATH, 'wb') as f, tqdm(
        desc=LLAMA_MODEL_PATH,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=8192):
            size = f.write(chunk)
            bar.update(size)
    
    print(f"Model downloaded and saved to {LLAMA_MODEL_PATH}")

if __name__ == "__main__":
    download_model()
