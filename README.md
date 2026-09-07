# AI-Powered Niche Market Sentiment Tracker

A personal learning project that analyzes public sentiment (positive/negative/neutral) 
on niche topics by reading public posts from Reddit and YouTube comments, then using 
an AI model to classify opinions.

## What it does
- Takes a keyword/topic as input (e.g. "mechanical keyboards")
- Searches public Reddit posts and YouTube comments mentioning that topic
- Runs the text through a sentiment analysis AI model
- Displays results: % positive/negative/neutral, sample posts, common themes

## Status
Work in progress — educational project, not for commercial use.

## Tech Stack
- Python (FastAPI backend)
- PRAW (Reddit API wrapper)
- YouTube Data API
- Hugging Face Transformers (sentiment analysis model)