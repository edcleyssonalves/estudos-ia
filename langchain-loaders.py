import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader


load_dotenv()

os.environ['OPENAI_API_KEY']

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    max_completion_tokens=500,

)

# loader = TextLoader('data/base_conhecimento.txt')
# documents = loader.load()

loader = PyPDFLoader('data/base_conhecimento.pdf')
documents = loader.load()

# loader = CSVLoader('data/base_conhecimento.csv')
# documents = loader.load()

prompt_knowledge_base = PromptTemplate(
    input_variables=['contexto', 'pergunta'],
    template='''
    Use o seguinte contexto para responder a pergunta.
    Responda apenas com base nas informações conhecidas.
    Não utilize informações externas ao contexto:
    Contexto: {contexto}
    Pergunta: {pergunta}
'''
)

chain = prompt_knowledge_base | model | StrOutputParser()

response = chain.invoke(
    {
        'contexto': '\n'.join(doc.page_content for doc in documents),
        'pergunta': 'Qual a diferença entre HTTP e HTTPS?',
    }
)

print(response)
