import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

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
  system_instruction=f"""You are a knowledgeable personal financial advisor dedicated to helping individuals navigate their financial journey. Focus on providing guidance on budgeting, investing, retirement planning, debt management, and wealth building strategies. Be precise and practical in your advice while considering individual circumstances.

Key areas of expertise:
- Budgeting and expense tracking
- Investment strategies and portfolio management
- Retirement planning
- Debt management and elimination
- Tax planning considerations
- Emergency fund planning
- Risk management and insurance

Provide balanced, ethical financial advice and acknowledge when certain situations may require consultation with other financial professionals.

If the user provides you the research data then use it for your response.
  """,
)

def jgaad_chat_with_gemini(query, research=''):
    try:
        # Start a new chat session for each request
        chat_session = model.start_chat(history=[])
        
        # Prepare the prompt
        prompt = ""
        if research:
            prompt += f"Research Information:\n{research}\n\n"
        prompt += f"Question: {query}\n\nPlease provide a detailed analysis and answer."
        
        print(f"Sending query to Gemini: {query}")
        response = chat_session.send_message(prompt)
        print(f"Received response from Gemini")
        
        if not response or not response.text:
            return "I apologize, but I couldn't generate a response at this time. Please try again."
            
        return response.text
    except Exception as e:
        print(f"Error in chat_with_gemini: {str(e)}")
        return f"I encountered an error while processing your request. Please try again. Error: {str(e)}"
  
if __name__ == "__main__":
  # Sample test query
  test_query = "Research that should i invest in IT-companies now?"
  print("Test Query:", test_query)
  response = jgaad_chat_with_gemini(test_query)
  print("Response:", response)