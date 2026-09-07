import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def fetch_posts(keyword: str, limit: int = 50):
    """Search Reddit for posts mentioning the keyword."""
    results = []
    
    for submission in reddit.subreddit("all").search(keyword, limit=limit):
        results.append({
            "text": submission.title + " " + (submission.selftext or ""),
            "score": submission.score,
            "url": f"https://reddit.com{submission.permalink}",
            "subreddit": str(submission.subreddit)
        })
    
    return results