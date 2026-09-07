from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from youtube_fetch import fetch_youtube_comments
from sentiment import analyze_batch

app = FastAPI(title="Niche Market Sentiment Tracker")

# Allow our future webpage (running on a different port) to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    """Simple check to confirm the API is alive."""
    return {"message": "Sentiment Tracker API is running"}


@app.get("/analyze")
def analyze_keyword(keyword: str):
    """
    Main endpoint. Call this with a keyword, e.g.:
    /analyze?keyword=mechanical keyboard
    """
    # Step 1: fetch comments about this keyword
    comments = fetch_youtube_comments(keyword, max_videos=5, max_comments_per_video=15)
    texts = [c["text"] for c in comments]

    if not texts:
        return {"error": "No comments found for this keyword. Try a different or broader term."}

    # Step 2: run sentiment analysis
    result = analyze_batch(texts)

    return {
        "keyword": keyword,
        "summary": result["summary"],
        "sample_results": result["results"][:10]  # only send back a sample, not all data
    }