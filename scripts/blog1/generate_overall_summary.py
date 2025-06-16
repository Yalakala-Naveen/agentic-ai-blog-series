from transformers import pipeline
from scripts.utils import load_json

def generate_overall_summary(summary_file="data/blog1_summaries.json"):
    summaries = load_json(summary_file)
    combined = " ".join(item["summary"] for item in summaries)

    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    overall = summarizer(combined[:3000], max_length=100, min_length=40, do_sample=False)
    print("\n🔮 Overall Summary:")
    print(overall[0]["summary_text"])
    return overall[0]["summary_text"]