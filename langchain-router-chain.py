import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

os.environ['OPENAI_API_KEY']

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    max_completion_tokens=500,

)

classification_chain = (
    PromptTemplate.from_template(
        '''
        Classifique a pergunta do usuário em um dos seguintes setores:
        - Financeiro
        - Suporte Técnico
        - Informações Gerais

        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

financial_support_chain = (
    PromptTemplate.from_template(
        '''
        Você é um especialista em suporte financeiro.
        Sempre responda as perguntas começando com "bem-vindo ao setor financeiro".
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

tech_support_chain = (
    PromptTemplate.from_template(
        '''
        Você é um especialista em suporte técnico.
        Sempre responda as perguntas começando com "bem-vindo ao suporte técnico".
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

other_support_chain = (
    PromptTemplate.from_template(
        '''
        Você é um especialista geral de suporte de todos os setores.
        Sempre responda as perguntas começando com "bem-vindo a central geral de suporte".
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)


def route(classification):
    classification = classification.lower()
    if 'financeiro' in classification:
        return financial_support_chain
    elif 'técnico' in classification:
        return tech_support_chain
    else:
        return other_support_chain

pergunta = input('Digite a sua pergunta: ')

classification = classification_chain.invoke(
    {'pergunta': pergunta}
)

print(f'Classificação: {classification}')

print('pergunta recebida, redirecionando para o setor responsável...')

response_chain = route(classification=classification)

response = response_chain.invoke(
    {'pergunta': pergunta}
)

print(response)
