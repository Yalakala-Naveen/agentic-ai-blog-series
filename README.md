# 📝 “I Built an AI Agent That Learned Agentic AI By Reading Blogs”
This project extracts the latest Agentic AI blog posts from Medium, summarizes each post using state-of-the-art NLP models, and generates an overall summary. The goal is to build an AI that learns from Agentic AI blogs and eventually writes blog content autonomously.

Project Structure:

Agentic_AI_Project/
├── assets/              # Static files such as images, icons, or any media used in blogs or docs
├── data/                # Raw and processed data files (e.g., scraped articles, summaries JSON)
├── logs/                # Logs for tracking script runs, errors, or other runtime info
├── notebooks/           # Jupyter notebooks for experimentation, demos, or analysis
├── scripts/             # Main project scripts, organized by blog or functionality
│   ├── blog1/
│   │   ├── extract_and_summarize.py
│   │   ├── generate_overall_summary.py
│   │   └── __init__.py
│   ├── blog2/
│   │   └── ...
│   ├── utils.py
│   └── main.py
├── requirements.txt     # Python dependencies
├── README.md            # Project overview and documentation
└── .gitignore           # Git ignore rules


Installation:

Clone the Project

Create a virtual environment (recommended):
 python3 -m venv genai_env
 source genai_env/bin/activate (On Windows use genai_env\Scripts\activate)
 

Install dependencies:
 pip install -r requirements.txt

Usage:

Run the main script to extract, summarize, and generate overall summaries of the latest Agentic AI blogs:

 python scripts/main.py

This will:

Fetch latest 10 blog posts from Medium tagged agentic-ai

Extract and summarize each blog post

Generate an overall summary combining all individual summaries

Save results to JSON files in the blogs/ folder

Adding New Blogs:

Create a new folder under scripts/ (e.g., blog2/)

Add scripts like extract_and_summarize.py, generate_overall_summary.py specific to the new blog

Use existing utils.py for common functions

Update main.py to call new blog scripts as needed

Future Work:

Integrate vector databases for semantic search

Implement LangChain or LangGraph for advanced Agentic AI workflows

Automate blog writing by AI agents based on learned summaries

Continuous monitoring and updating as new Agentic AI blogs appear

Contact:
Your Name — yalakalanaveen789@gmail.com

Project Link: https://github.com/YALAKALA-NAVEEN/agentic-ai-blog-series
