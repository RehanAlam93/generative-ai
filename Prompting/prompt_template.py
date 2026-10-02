from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")

question = "explain machine learning"
response = llm.invoke(question)
print("final output : ", response)

# prompt in langchain  ---->
prompt = PromptTemplate.from_template(
    "Explain {topic} in English"
)

prompt_value = prompt.invoke(
    {
        "topic": "machine learning"
    }
)

llm = ChatOllama(model="llama3.2:1b")
response = llm.invoke(prompt_value)
print(response.content)

chat = ChatOllama(model="llama3.2:1b")
response = chat.invoke(
    [
        SystemMessage(
            content="You are a helpful assistant that translates English to French."
        ),
        HumanMessage(
            content="what is the capital of France?"
        )
    ]
)
print(response.content)
