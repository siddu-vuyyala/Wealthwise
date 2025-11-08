import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

print(f"Using API key: {api_key[:5]}...")
genai.configure(api_key=api_key)

# List all available models
print("\nAvailable models:")
for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(f"- {model.name} ({', '.join(model.supported_generation_methods)})")