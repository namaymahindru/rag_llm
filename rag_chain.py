from langchain_openai import ChatOpenAI         # ← changed
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from embedder import get_retriever
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

SYSTEM_PROMPT = """
You are a helpful reading assistant. Answer the user's question
based ONLY on the article chunks provided below as context.

If the answer is not in the context, say:
"I couldn't find information about that in your saved articles."

Always mention which article (title/source) your answer came from.

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}"),
])

def ask_question(question: str) -> dict:
    retriever = get_retriever()
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)
    result = rag_chain.invoke({"input": question})
    
    return {
        "answer": result["answer"],
        "sources": [doc.metadata for doc in result["context"]]
    }