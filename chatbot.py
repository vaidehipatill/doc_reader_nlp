# Handles OpenAI GPT chat

import openai

# Set OpenAI API key
OPENAI_API_KEY = "PLEASE_USE_YOUR_API_KEY"

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def chat_with_gpt(context, question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant answering based on the document."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"}
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()
