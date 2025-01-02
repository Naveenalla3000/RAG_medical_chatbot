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

from src.main import load_pdf, text_split, load_embedding_model

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")


extracted_data = None
extracted_data = load_pdf("./data/")
text_chunks = text_split(extracted_data)
embeddings = load_embedding_model()
pc = PineconeClient(api_key=PINECONE_API_KEY)
index_name = PINECONE_INDEX_NAME
index = pc.Index(index_name)
if index.exists():
    index.delete()
dosearch = PineconeVectorStore.from_texts(
    [
        tc.page_content for tc in text_chunks
    ],
    embeddings,
    index_name=index_name,
)