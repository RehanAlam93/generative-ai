from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3.2:1b")
response = llm.invoke("what is the capital of France?")
print(response)

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import dotenv

OPENAI_API_KEY = " "

from dotenv import load_dotenv
load_dotenv()

# Initialize the gemnai chat model
llm = ChatOpenAI(model="gpt-4o",temperature=0,api_key=OPENAI_API_KEY
)
response = llm.invoke("hello hii")
print(response)
chat = ChatOllama(model="llama3.2:1b")
response = chat.invoke([
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(
        content="what is the capital of France?"
    )
])
print(response.content)

# gemnai
import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0)
response = llm.invoke([
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(
        content="what is the capital of France?"
    )
])
print(response.content)

