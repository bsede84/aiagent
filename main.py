import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

parser = argparse.ArgumentParser(description='A sample script that accepts command-line arguments.')
parser.add_argument('--verbose', action='store_true', help='Enable verbose output.')
parser.add_argument('user_prompt', nargs='+', help='The user prompt to send to the model.')
# Parse args after all arguements have been defined
args = parser.parse_args()

if len(sys.argv) > 1:
    user_prompt = " ".join(args.user_prompt)
else:
    print("No arguments provided.")
    sys.exit(1)

messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)

if args.verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")