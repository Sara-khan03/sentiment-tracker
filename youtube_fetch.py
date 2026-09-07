import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

youtube = build("youtube", "v3", developerKey=os.getenv("YOUTUBE_API_KEY"))

def fetch_youtube_comments(keyword: str, max_videos: int = 5, max_comments_per_video: int = 20):
    """Search YouTube for videos about the keyword, then pull comments from them."""
    results = []

    # Step 1: search for videos matching the keyword
    search_response = youtube.search().list(
        q=keyword,
        part="id",
        maxResults=max_videos,
        type="video"
    ).execute()

    video_ids = [item["id"]["videoId"] for item in search_response.get("items", [])]

    # Step 2: pull comments from each video found
    for video_id in video_ids:
        try:
            comments_response = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=max_comments_per_video,
                textFormat="plainText"
            ).execute()

            for item in comments_response.get("items", []):
                comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                results.append({
                    "text": comment_text,
                    "video_id": video_id,
                    "url": f"https://youtube.com/watch?v={video_id}"
                })
        except Exception as e:
            # Some videos have comments disabled — skip those instead of crashing
            print(f"Skipped video {video_id}: {e}")
            continue

    return results