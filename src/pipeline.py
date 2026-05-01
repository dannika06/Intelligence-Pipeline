import os
from docling.document_converter import DocumentConverter

INPUT_DIR = "input_docs"
OUTPUT_DIR = "outputs"

def process_document(file_path, converter):
    try:
        result = converter.convert(file_path)
        content = result.document.export_to_markdown()
        return content
    except Exception as e:
        print(f"[ERROR] Failed to process {file_path}: {e}")
        return f"# Error processing document\n\n{str(e)}"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    converter = DocumentConverter()

    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith((".pdf", ".docx", ".pptx")):
            continue

        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename.split('.')[0] + ".md")

        print(f"Processing: {filename}")
        content = process_document(input_path, converter)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()