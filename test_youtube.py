from youtube_fetch import fetch_youtube_comments

results = fetch_youtube_comments("mechanical keyboard review", max_videos=2, max_comments_per_video=5)

print(f"Total comments fetched: {len(results)}")
print("---")
for r in results[:5]:
    print(r["text"][:100])
    print("---")