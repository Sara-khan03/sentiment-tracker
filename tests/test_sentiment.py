import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sentiment import analyze_batch
from youtube_fetch import fetch_youtube_comments

print("Fetching YouTube comments...")
comments = fetch_youtube_comments("mechanical keyboard review", max_videos=3, max_comments_per_video=10)
texts = [c["text"] for c in comments]

print(f"Fetched {len(texts)} comments. Now analyzing sentiment...\n")

result = analyze_batch(texts)

print("=== SUMMARY ===")
print(f"Total comments: {result['summary']['total']}")
print(f"Positive: {result['summary']['positive_percent']}%")
print(f"Negative: {result['summary']['negative_percent']}%")
print("\n=== SAMPLE RESULTS ===")
for r in result["results"][:5]:
    print(f"[{r['sentiment']['label']} - {r['sentiment']['score']}] {r['text'][:80]}")