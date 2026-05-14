import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

os.environ['OPENAI_API_KEY']

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    max_completion_tokens=500,

)

template = '''
Traduza o teto do {idioma1} para o {idioma2}:
{texto}
'''

prompt_template = PromptTemplate.from_template(
    template=template
)

prompt = prompt_template.format(
    idioma1='Português',
    idioma2='Inglês',
    texto='Boa tarde',
)

response = model.invoke(prompt)

print(response.content)
