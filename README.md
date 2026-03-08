# 📖 Smart Article Reader — RAG Project

A beginner-friendly **Retrieval-Augmented Generation (RAG)** app that lets you save articles and chat with your reading collection using AI.

## 🚀 Features
- 🔗 Save any article by URL
- 🤖 Ask questions across all saved articles
- 📚 Get cited answers (with source links)
- 💾 Persistent vector storage with ChromaDB
- ⚡ Powered by LangChain + OpenAI

## 🏗️ Architecture

```
Article URL → Scrape → Chunk → Embed → ChromaDB
                                           ↑
User Question → Embed → Vector Search ────┘
                             ↓
                    Top 3 Chunks → GPT-4o-mini → Answer
```

## 🛠️ Tech Stack

| Component     | Tool                        |
|---------------|-----------------------------|
| Web Scraping  | `trafilatura`               |
| Chunking      | `LangChain RecursiveCharacterTextSplitter` |
| Embeddings    | `OpenAI text-embedding-3-small` |
| Vector DB     | `ChromaDB` (local)          |
| LLM           | `GPT-4o-mini`               |
| Framework     | `LangChain`                 |
| UI            | `Streamlit`                 |

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/rag_llm.git
cd rag_llm
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=sk-your-openai-key-here
```

> ⚠️ Never commit your `.env` file. It's already in `.gitignore`.

### 5. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

## 📁 Project Structure
```
rag_llm/
├── .env                # API keys (not in git)
├── .gitignore
├── requirements.txt
├── app.py              # Streamlit UI
├── scrapper.py         # Article scraping
├── chunker.py          # Text splitting
├── embedder.py         # Embeddings + ChromaDB
└── rag_chain.py        # LangChain RAG pipeline
```

## 📚 How It Works

1. **Save Article** → Paste a URL, trafilatura scrapes clean text
2. **Chunking** → Article is split into ~1000 char overlapping chunks
3. **Embedding** → Each chunk converted to a 1536-dim vector via OpenAI
4. **Storage** → Vectors saved in local ChromaDB
5. **Query** → Your question is embedded, top-3 similar chunks retrieved
6. **Answer** → GPT-4o-mini generates answer from retrieved chunks

## 🧠 Concepts Learned
- RAG (Retrieval-Augmented Generation)
- Vector Embeddings & Semantic Search
- Text Chunking strategies
- LangChain chains and retrievers
- ChromaDB vector database
- Prompt engineering
