import feedparser
import os
from newspaper import Article
from transformers import pipeline
import time
from scripts.utils import save_json

def extract_and_summarize(n=10, output_path=None):
    if output_path is None:
        # fallback to default relative path in root/data
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_path = os.path.join(PROJECT_ROOT, "data", "blog1_summaries.json")
        
    print(f"🔍 Fetching latest {n} Agentic AI posts from Medium...")
    MEDIUM_RSS = "https://medium.com/feed/tag/agentic-ai"
    feed = feedparser.parse(MEDIUM_RSS)
    entries = feed.entries[:n]

    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    all_summaries = []

    for i, entry in enumerate(entries, 1):
        url = entry.link
        title = entry.title
        print(f"\n#{i}: {title}\nURL: {url}")
        try:
            article = Article(url)
            article.download()
            article.parse()
            text = article.text

            if len(text) < 100:
                print("⚠️ Skipping short article.")
                continue

            truncated_text = text[:1000]
            summary = summarizer(truncated_text, max_length=60, min_length=20, do_sample=False)
            summary_text = summary[0]["summary_text"]

            print("📝 Summary:", summary_text)
            all_summaries.append({
                "title": title,
                "url": url,
                "summary": summary_text
            })
            time.sleep(1)
        except Exception as e:
            print(f"❌ Error processing {url}: {e}")

    save_json(all_summaries, output_path)
    return all_summaries