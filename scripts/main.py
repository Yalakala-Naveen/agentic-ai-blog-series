import warnings
warnings.filterwarnings("ignore")

import os

# Get absolute path of project root (parent of scripts folder)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build absolute path for json file under root/data/
json_path = os.path.join(PROJECT_ROOT, "data", "blog1_summaries.json")

from scripts.blog1.extract_and_summarize import extract_and_summarize
from scripts.blog1.generate_overall_summary import generate_overall_summary

def main():
    print("🚀 Starting Blog 1 Agentic AI Summarizer...")
    summaries = extract_and_summarize(n=10)
    if summaries:
        generate_overall_summary()
    print("\n✅ Blog 1 processing complete.")

if __name__ == "__main__":
    main()
