
## build an application that will take user input, pass it through OpenAI model  and return the response

# load the env variables from .env file
from dotenv import load_dotenv
load_dotenv()

#  Take user input

user_input = input("Please enter your question:")

print(user_input)

# make an LLm call to openai
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model= "gpt-4o-mini",
    messages= [
        {"role": "system", "content":"you are a helpful assisstant."},
        {"role": "user", "content":user_input}
    ]
)

print(response.choices[0].message.content)
