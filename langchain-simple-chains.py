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

# prompt_template = PromptTemplate.from_template(
#     'Me fale sobre normatizações ISO/IEC {normatizacoes}'
# )

# runnable_sequence = prompt_template | model | StrOutputParser()

runnable_sequence = (
    PromptTemplate.from_template(
        'Me fale sobre normatizações ISO/IEC {normatizacoes}'
    )
    | model
    | StrOutputParser()
)

response = runnable_sequence.invoke({'normatizacoes': 'Iso 27001'})

print(response)

# output
# A norma ISO/IEC 27001 é um padrão internacional de segurança da informação que estabelece
# requisitos e controles para a implementação, monitoramento e melhoria de um Sistema de Gestão de Segurança da Informação (SGSI).
# Essa norma visa garantir a proteção e a segurança dos ativos de informação de uma organização, incluindo dados confidenciais, sistemas de informação,
# recursos humanos, entre outros.
# Alguns dos principais requisitos da ISO/IEC 27001 incluem a análise de riscos, definição de uma política de segurança da informação,
# estabelecimento de controles de segurança adequados, treinamento dos colaboradores, monitoramento e avaliação do desempenho do SGSI, entre outros.
# A certificação na ISO/IEC 27001 é prova de que uma organização adota boas práticas de segurança da informação e demonstra comprometimento com a proteção
# dos dados e informações confidenciais. É importante ressaltar que a certificação não é obrigatória, mas pode ser um diferencial competitivo no mercad
# o e transmitir confiança aos clientes, parceiros e colaboradores.
