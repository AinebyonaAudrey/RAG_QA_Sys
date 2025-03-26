import os
import openai

API_HOST = os.getenv("API_HOST", "github")
client = openai.OpenAI(base_url="https://models.inference.ai.azure.com", api_key=os.environ["GITHUB_TOKEN"])
MODEL_NAME = os.getenv("GITHUB_MODEL","gpt-4o")
