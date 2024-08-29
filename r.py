import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Instantiate the OpenAI client with the API key from the environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=1):
    completion = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=messages,
    )
    return completion.choices[0].message.content

def get_image(prompt):
    image = client.images.generate(
        model="dall-e-3",
        prompt = prompt,
        size = "1024x1024",
        quality = "standard",
        n=1
    )
    return image.data[0].url

messages=[
      {"role": "system", "content": "You are an Instagram content creator who likes anime. \
                                       You will generate 1 recipe from a popular anime with emojis that are less than 900 characters long from different anime. the first line must be a title (do not label it with title) with the recipe and anime name"},
      {"role": "user", "content": "I want to create content on healthy diets."}

  ]
temperatures = [1, 1, 1, 1]

for temperature in temperatures:
    print(f"Temperature: {temperature}")
    content = get_completion_from_messages(messages=messages, temperature=temperature)
    print(content)

    #Getting the title
    lines = content.split('\n')
    title = lines[0].strip()

    # Create an image based on the title
    prompt = f"{title}"
    image = get_image(prompt)
    print("Image URL:", image)
