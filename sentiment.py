from transformers import pipeline

# Load the AI model once when the app starts (this takes a few seconds the first time)
print("Loading sentiment analysis model... (this may take a moment on first run)")
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
print("Model loaded successfully!")


def analyze_sentiment(text: str):
    """
    Takes a piece of text and returns its sentiment label and confidence score.
    Returns something like: {"label": "POSITIVE", "score": 0.9987}
    """
    if not text or not text.strip():
        return {"label": "NEUTRAL", "score": 0.0}

    # The model only accepts up to 512 tokens, so we trim very long text
    trimmed_text = text[:1000]

    result = sentiment_model(trimmed_text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }


def analyze_batch(texts: list):
    """Analyze a list of texts and return sentiment for each, plus a summary."""
    results = []
    positive_count = 0
    negative_count = 0

    for text in texts:
        sentiment = analyze_sentiment(text)
        results.append({"text": text, "sentiment": sentiment})

        if sentiment["label"] == "POSITIVE":
            positive_count += 1
        elif sentiment["label"] == "NEGATIVE":
            negative_count += 1

    total = len(texts) if texts else 1
    summary = {
        "total": len(texts),
        "positive_percent": round((positive_count / total) * 100, 1),
        "negative_percent": round((negative_count / total) * 100, 1),
    }

    return {"results": results, "summary": summary}