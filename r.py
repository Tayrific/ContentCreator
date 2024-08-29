import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Instantiate the OpenAI client with the API key from the environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    completion = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=messages,
    )
    return completion.choices[0].message.content

messages=[
      {"role": "system", "content": "You are an Instagram content creator who likes anime. \
                                       You will generate 1 recipe from a popular anime with emojis that are less than 500 characters long."},
      {"role": "user", "content": "I want to create content on easy balanced diets."}

  ]
temperatures = [0, 0.5, 0.8, 1]

for temperature in temperatures:
    print(f"Temperature: {temperature}")
    content = get_completion_from_messages(messages=messages, temperature=temperature)
    print(content)
