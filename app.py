import chainlit as cl
import os
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.agents import Agent
from langchain.chat_models import openai,ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone as PineconeClient
from typing import Dict, Optional
from literalai import LiteralClient
from src.main import load_embedding_model,load_llm_model
from src.prompt_template import prompt_template

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
LITERAL_API_KEY = os.getenv("LITERAL_API_KEY")

lai = LiteralClient(api_key=LITERAL_API_KEY)
lai.instrument_openai()

embeddings = load_embedding_model() 

pc = PineconeClient(api_key=PINECONE_API_KEY)
index_name = PINECONE_INDEX_NAME

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

PROMPT=PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question","history"]
)

conversationBufferMemory = ConversationBufferMemory(
    memory_key="history",
    return_messages=True,
    input_key="question"
)

chain_type_kwargs={
    "prompt": PROMPT,
    "memory": conversationBufferMemory
}

llm = load_llm_model()

rqa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={'k': 3}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs,
)

@cl.on_message
async def main(message: cl.Message):
    print("on_message", message.content)
    response =  rqa.invoke({"query": message.content})
    result = response["result"]
    await cl.Message(content=result).send()

@cl.on_chat_start
async def on_chat_start():
    app_user = cl.user_session.get("user")
    await cl.Message(f"Hello {app_user.identifier}, Welcome to medical chatbot").send()

@cl.oauth_callback
def oauth_callback(
  provider_id: str,
  token: str,
  raw_user_data: Dict[str, str],
  default_user: cl.User,
) -> Optional[cl.User]:
  return default_user