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



meta_prompt = """
Act as an expert prompt optimizer. Your task is to rewrite the provided prompt to be more detailed, specific, and effective for an LLM.

CRITICAL OUTPUT RULES:
1. Output ONLY the raw text of the improved prompt.
2. Do NOT include any headers (e.g., "Constraints:", "Perfected Prompt:", "Analysis:").
3. Do NOT include any introductory or concluding remarks.
4. Do NOT answer the user's prompt.

Original Prompt: "{user_prompt}"

Optimized Prompt:
"""
try:
    model=genai.GenerativeModel('gemini-2.5-flash')
    raw_prompt=input("Enter a prompt: ")

    full_prompt=meta_prompt.format(user_prompt=raw_prompt)
    print("\n... Perfection in progress...\n")
    response=model.generate_content(full_prompt)
    print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")
