# import json
import openai
import os

openai.api_key = "sk-0Wp7yTPSqiI1DyHFT9VLT3Blb........................."

# system messages first, it helps set the behavior of the assistant.
messages = [{"role": "system",
             "content": "You are a helpful assistant."}]

while True:
    message = input("🫠: ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    reply = chat_completion.choices[0].message.content
    print(f"🧁:{reply}")
    messages.append({"role": "assistant", "content": reply})
