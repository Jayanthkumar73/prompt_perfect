import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if not GOOGLE_API_KEY:
    print("❌ Error: GOOGLE_API_KEY not found in .env file")
    exit(1)

genai.configure(api_key=GOOGLE_API_KEY)



meta_prompt='''
You are an expert prompt engineer. Your role is to take a user's simple prompt and rewrite it to be more detailed, specific, and effective for a generative AI.

You should enhance the prompt by:
1. Adding specific context and background.
2. Defining a clear structure or format for the desired output.
3. Specifying a tone or persona for the AI to adopt.
4. Including constraints or negative prompts to avoid unwanted content.
5. Ensuring the core intent of the original prompt is preserved and clarified.

User's Raw Prompt: "{user_prompt}"

Your Perfected Prompt:
'''
try:
    model=genai.GenerativeModel('gemini-2.5-flash')
    raw_prompt=input("Enter a prompt: ")

    full_prompt=meta_prompt.format(user_prompt=raw_prompt)
    print("\n... Perfection in progress...\n")
    response=model.generate_content(full_prompt)
    print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")
