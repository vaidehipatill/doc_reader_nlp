# Handles OpenAI GPT chat

import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(context, question):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": question}
        ]
    )

    # Extract the response content
    answer = response.choices[0].message.content.strip()
    return answer