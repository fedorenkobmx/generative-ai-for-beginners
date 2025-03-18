import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

model_name = "gpt-4o-mini"

client = OpenAI(
    api_key=api_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an art critic.",
        },
        {
            "role": "user",
            "content": "Describe the painting 'Starry Night' by Vincent van Gogh. Focus on the brushstrokes, colors, and emotional impact of the painting.",
        },
    ],
    model=model_name,
    temperature=1.,
    max_tokens=1000,
    top_p=1.    
)

print(response.choices[0].message.content)
