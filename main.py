
# key is the API token generated via Hugging Face
key = "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"

import json
import requests

headers = {"Authorization": f"Bearer {key}"}
API_URL = "https://api-inference.huggingface.co/models/gpt2"

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

# Stochastic methods
top_p_params = {"max_length": 128, "top_p": 0.95, "do_sample":True}
top_k_params = {"max_length": 128,  "top_k": 4, "do_sample":True}
# Contrastive Search
contrastive_params = {"max_length": 128, "penalty_alpha": 0.6, "top_k": 4}

text = input()

data = query({"inputs": text})
# Improving performance using stochastic  and contrastive methods
data1 = query({"inputs": text,
               "top_p": top_p_params})
data2 = query({"inputs": text,
               "top_k": top_k_params})
data3 = query({"inputs": text,
               "parameters": contrastive_params})

print(data)
print("Top-p output:", data1)
print("Top-k output:", data2)
print("Contrastive search output:", data3)
