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
print("\nAvailable models that support text generation:")
available_models = []
for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(f"- {model.name}")
        available_models.append(model.name)

# Test different model names
test_models = [
    "gemini-pro",
    "models/gemini-pro",
    "models/gemini-2.5-pro"
]

print("\nTesting models:")
for model_name in test_models:
    print(f"\nTrying model: {model_name}")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello!")
        print(f"Success! Model {model_name} works.")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error with {model_name}: {str(e)}")