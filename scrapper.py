import trafilatura



def scrape_article(url: str) -> dict:

    """
    Given a URL, downloads and extracts clean article text.
    Returns a dict with title, text, and url.
    """

    downloaded = trafilatura.fetch_url(url)

    if not downloaded:
        return {"error": "Failed to download the article"}
        

    text = trafilatura.extract(
        downloaded,
        include_comments= False,
        include_tables = False

    )
    metadata = trafilatura.extract_metadata(downloaded)

    title = metadata.title if metadata else url

    if not text:
        return {"error": "Failed to extract text from the article"}

    return {
        "url": url,
        "title": title,
        "text": text
    }    