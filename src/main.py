import os
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.agents import Agent
from langchain.chat_models import openai,ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone as PineconeClient

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

def load_pdf(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader,
    )
    documents = loader.load()
    return documents

def text_split(extracted_data):
    text_spliter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    text_chunks = text_spliter.split_documents(extracted_data)
    return text_chunks

def load_embedding_model():
    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY,model="text-embedding-3-large")
    return embeddings

def load_llm_model():
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o")
    return llm