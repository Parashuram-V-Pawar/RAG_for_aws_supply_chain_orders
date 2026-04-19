
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class Generator:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate(self, query, results):
        context = "\n".join(results['text'].tolist())

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a supply chain analyst. Answer only using the given data."
                },
                {
                    "role": "user",
                    "content": f"""
                    Data:
                    {context}

                    Question:
                    {query}
                    """
                }
            ]
        )

        return response.choices[0].message.content