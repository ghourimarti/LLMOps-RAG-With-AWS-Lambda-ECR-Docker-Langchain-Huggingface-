import json
import os
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("cr.env")

prompt = """
You are a smart assistant so please let me know what is machine learning in the smartest way?
"""

# Bedrock runtime client (credentials loaded via AWS CLI config or env)
bedrock = boto3.client("bedrock-runtime")

# ✅ CORRECT payload for meta.llama3-70b-instruct-v1:0
payload = {
    "prompt": prompt,
    "max_gen_len": 512,
    "temperature": 0.3,
    "top_p": 0.9
}

model_id = "meta.llama3-70b-instruct-v1:0"

body = json.dumps(payload)

response = bedrock.invoke_model(
    modelId=model_id,
    body=body,
    contentType="application/json",
    accept="application/json"
)

# ✅ Correct key expected in response
response_body = json.loads(response["body"].read().decode("utf-8"))
response_text = response_body.get("generation", "[No response text found]")
print(f"Response from model: {response_text}")
