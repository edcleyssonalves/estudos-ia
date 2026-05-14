import os
from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

os.environ['OPENAI_API_KEY']

# model = OpenAI()

# response = model.invoke(
#     input='Quem foi Linux Torvalds',
#     temperature=0.7,
#     max_tokens=500,
# )

# print(response)

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    max_completion_tokens=500,
)

messages = [
    {'role': 'system', 'content':'Você é um assistente que fornece informações sobre TI e Programação'},
    {'role': 'user', 'content':'O que é um movimento de exploração lateral?'}
]

response = model.invoke(messages)

print(response)
print(response.content)