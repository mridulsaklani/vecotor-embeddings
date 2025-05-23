from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

text = "Maharana Pratap is one of the greatest Rajput warriors"

response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small"
)

print("Vector embedding:", response.data[0].embedding)



