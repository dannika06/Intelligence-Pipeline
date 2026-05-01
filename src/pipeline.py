import os
from docling.document_converter import DocumentConverter
import gc 
# Add to be able to create PR
# Base directory (directory where this script lives)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define input/output directories relative to project root
INPUT_DIR = os.path.join(BASE_DIR, "..", "input_docs")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "outputs")


def process_document(file_path, converter):
    try:
        result = converter.convert(file_path)
        content = result.document.export_to_markdown()
        return content
    except Exception as e:
        print(f"[ERROR] Failed to process {file_path}: {e}")
        return f"# Error processing document\n\n{str(e)}"


def main():
    # Ensure directories exist
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    converter = DocumentConverter()

    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith((".pdf", ".docx", ".pptx")):
            continue

        input_path = os.path.join(INPUT_DIR, filename)
        output_filename = os.path.splitext(filename)[0] + ".md"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        print(f"Processing: {filename}")
        content = process_document(input_path, converter)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Saved: {output_path}")

        gc.collect()


if __name__ == "__main__":
    main()