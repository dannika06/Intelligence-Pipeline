# Report: Document Intelligence Pipeline

## Tool / Library Evaluation

For this project, I chose to use Docling as the primary document processing library. The main reason for this choice was its ability to handle multiple file formats (PDF, DOCX, PPTX) and convert them directly into structured Markdown with minimal setup.

One of Docling’s strengths is its simplicity. It allows for quick integration and produces reasonably structured output without requiring extensive configuration. This makes it well-suited for a project focused on building a working pipeline rather than optimizing extraction accuracy.

However, the library has some limitations. Table extraction is inconsistent, and formatting is often lost or simplified. Additionally, complex layouts such as multi-column documents are not always processed correctly, leading to issues with reading order. Image extraction is also limited or absent.

## Failure Modes

One failure mode observed was with multi-column PDFs. In these cases, the extracted text appeared out of order, making the output difficult to read. I chose not to implement a fix for this due to time constraints and the complexity of layout analysis, but documented it as a known limitation.

Another issue occurred with scanned PDFs. Since these documents do not contain selectable text, the pipeline was unable to extract meaningful content. Instead of crashing, the system logs an error and produces a partial output file with an error message. This ensures the pipeline remains robust even when encountering unsupported inputs.

## Real-World Applications

This type of pipeline has several practical applications. One use case is resume parsing, where large volumes of resumes can be converted into structured formats for easier analysis. Another application is legal document processing, where contracts and agreements can be extracted and indexed. A third use case is academic research, where papers can be converted into structured text for summarization or search.

## Design Decision

One key design decision was to use Markdown as the output format instead of JSON. While JSON is more structured and machine-readable, Markdown is significantly easier for humans to read and review. Since the focus of this project is peer review and communication, Markdown provides a better balance between structure and readability.

Additionally, the pipeline was designed with simplicity in mind. The code is organized into a single script with clear logic and basic error handling. This makes it easy for reviewers to understand how the system works without needing to navigate a complex codebase.