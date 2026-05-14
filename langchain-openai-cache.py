import os
from dotenv import load_dotenv
from langchain_community.cache import SQLiteCache
from langchain_core.globals import set_llm_cache
from langchain_openai import OpenAI


load_dotenv()

os.environ['OPENAI_API_KEY']

model = OpenAI()

set_llm_cache(
    SQLiteCache(database_path='openai_cache.db')  # cria banco de dados sqlite se ainda não existir
)

prompt = 'O que é um movimento de exploração lateral em segurança da informação?'

response1 = model.invoke(prompt)
print(f'Chamada 1: {response1}')

response2 = model.invoke(prompt)
print(f'Chamada 2: {response2}')
