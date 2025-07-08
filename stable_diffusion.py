import json
import os
import base64
import boto3
from dotenv import load_dotenv

# Load AWS credentials from .env file
load_dotenv("cr.env")

# Initialize Bedrock Runtime Client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

# Your text prompt
prompt = "A realistic 4K ultra HD image of a person who is standing on a mountain peak, with a breathtaking view of the valley below, during sunset. The sky is filled with vibrant colors of orange, pink, and purple, and the person is wearing a warm jacket and a beanie. The scene captures the essence of adventure and tranquility."

# Payload for Titan G1 (v1)
payload = {
    "taskType": "TEXT_IMAGE",
    "textToImageParams": {
        "text": prompt
    },
    "imageGenerationConfig": {
        "numberOfImages": 1,
        "quality": "standard",     # or "premium"
        "height": 1024,
        "width": 1024,
        "cfgScale": 8.0,
        "seed": 0
    }
}

# ✅ Correct model ID
model_id = "amazon.titan-image-generator-v1"

# Convert payload to JSON
body = json.dumps(payload)

# Invoke the Titan model
response = bedrock.invoke_model(
    modelId=model_id,
    body=body,
    contentType="application/json",
    accept="application/json"
)

# Parse the response
response_body = json.loads(response["body"].read().decode("utf-8"))
base64_image = response_body["images"][0]

# Save the image
output_dir = "output_images"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "titan_image_v1.png")

with open(output_path, "wb") as f:
    f.write(base64.b64decode(base64_image))

print(f"✅ Image saved to: {output_path}")
