from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text: str, url: str, title: str) -> list:

    """
    Splits a large article into smaller overlapping chunks.
    Each chunk keeps metadata (source URL, title).
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,       # Each chunk = ~1000 characters
        chunk_overlap=200,     # 200 chars overlap between chunks
        separators=["\n\n", "\n", ". ", " "]  # Split priority
    ) 

    chunks = splitter.create_documents(
        [text],
        metadatas=[
            {
                "source": url,
                "title": title
            }
        ]
    )

    return chunks