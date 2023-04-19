import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.Completion.create(
    model="text-davinci-003",
    prompt ="What is the capital of France?",
    max_tokens=7,
)
print(response)
print(response['choices'][0]['text'])