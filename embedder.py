from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")

CHROMA_PATH = "./chroma_db"

def get_vector_store():
    return Chroma(collection_name="articles", embedding_function=embeddings, persist_directory=CHROMA_PATH)


def add_chunks_to_store(chunks: list):
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)

    print(f"✅ Added {len(chunks)} chunks to vector store")

def get_retriever():
    vector_store = get_vector_store()
    

    return vector_store.as_retriever(

        search_type = "similarity",
        search_kwargs = {
            "k": 3
        }
    )
    

