
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
data = query({"inputs": "Wanted to get some insughts as to what a Large Language Model can do"})
print(data)
