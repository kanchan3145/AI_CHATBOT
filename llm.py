from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_llm(question):

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role":"user",
                    "content":question
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        print("ERROR:", e)

        return "AI service is currently unavailable."