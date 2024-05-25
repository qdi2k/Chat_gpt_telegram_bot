import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()
client = AsyncOpenAI(
    api_key=os.getenv('LLAMA_TOKEN'),
    base_url="https://api.llama-api.com"
)


async def gpt4(question):
    response = await client.chat.completions.create(
        model="llama-13b-chat",
        messages=[
            {"role": "system",
             "content": "Отвечай на русском языке"},
            {"role": "user",
             "content": question}
        ])
    return response
