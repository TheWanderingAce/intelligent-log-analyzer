from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {'role': 'user', 'content': 'Hello, I am a clanker'}
    ]
)

print(response.choices[0].message.content)