import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

print(f"Using API key: {api_key[:5]}...")
genai.configure(api_key=api_key)

# List available models
print("Available models:")
for m in genai.list_models():
    print(m.name)

# Create the model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.8,
    "top_k": 40,
    "max_output_tokens": 2048,
}

try:
    # Using the latest pro model available
    model = genai.GenerativeModel('models/gemini-2.5-pro', generation_config=generation_config)
    print("Successfully created Gemini model")
except Exception as e:
    print(f"Error creating model: {str(e)}")
    raise

# Test the model
test_prompt = "Say hello and introduce yourself as an AI financial assistant"
try:
    response = model.generate_content(test_prompt)
    print("Response from Gemini:")
    print(response.text)
    print("\nTest successful!")
except Exception as e:
    print(f"Error: {str(e)}")