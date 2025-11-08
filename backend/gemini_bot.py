import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 0.7,
  "top_p": 0.8,
  "top_k": 40,
  "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
  model_name="models/gemini-2.5-pro",
  generation_config=generation_config,
  safety_settings=[
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
  ],
)

chat_session = model.start_chat(
  history=[
  ]
)

def chat_with_gemini(message, media_file_path=None):
  global chat_session
  files = []
  if media_file_path:
    for media_file in media_file_path:
      files.append(upload_to_gemini(media_file, mime_type="audio/mpeg"))
  
    response = chat_session.send_message(message, media_files=files)
    return response
  else:
    response = chat_session.send_message(message)
    return response.text
  
if __name__ == "__main__":
  # Sample test query
  test_query = "Research that should i invest in IT-companies now?"
  print("Test Query:", test_query)
  response = chat_with_gemini(test_query)
  print("Response:", response)