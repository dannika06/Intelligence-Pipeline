# Document Intelligence Pipeline

## Overview
This project implements a simple document intelligence pipeline that processes real-world documents (PDF, DOCX, PPTX) and converts them into structured Markdown output. The goal is to demonstrate a complete, end-to-end system that is easy to review, handles errors gracefully, and produces usable structured data.

## Features
- Batch processing of multiple documents
- Converts documents into Markdown format
- Extracts structured elements such as headers, lists, and tables (best effort)
- Graceful error handling (no crashes on bad files)
- Automatically saves outputs to a dedicated folder

## Tech Stack
- Python
- Docling (IBM document conversion library)

## Project Structure
```
intelligence-pipeline/
│
├── input_docs/
│   ├── doc1.pdf
│   ├── doc2.pdf
│   └── doc3.pdf
│
├── outputs/
│   ├── doc1.md
│   ├── doc2.md
│   └── doc3.md
│
├── src/
│   └── pipeline.py
│
├── README.md
├── REPORT.md
├── requirements.txt
└── REVIEW_NOTES.md
```

## Setup Instructions

1. Clone the repository: 
git clone https://github.com/dannika06/Intelligence-Pipeline.git
cd intelligence-pipeline

2. Install dependencies:
pip install -r requirements.txt


3. Add documents to the `input_docs/` folder

## How to Run

Run the pipeline with a single command:
python src/pipeline.py


## Output

- Processed files will be saved in the `outputs/` folder
- Each input file generates a corresponding `.md` file

Example: input_docs/resume.pdf → outputs/resume.md


## Notes

- This project prioritizes readability and reviewability over perfect extraction accuracy
- Some formatting (especially tables and images) may not convert perfectly
