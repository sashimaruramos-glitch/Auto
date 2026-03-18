import PyPDF2


def analyze_pdf(file_path):
    """
    Analyzes a PDF file for:
    - Page count
    - Paper size
    - Color detection
    """
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        page_count = len(pdf_reader.pages)
        print(f"Page Count: {page_count}")

        # Assuming A4 paper size as standard (for simplicity)
        for page in pdf_reader.pages:
            media_box = page.mediaBox
            width = media_box.getWidth()
            height = media_box.getHeight()
            print(f"Page Size: {width} x {height}")

        # Color detection placeholder
        # Implement color detection logic as needed
        # This is a complex task and requires more libraries

        return page_count

if __name__ == '__main__':
    file_path = 'your_pdf_file.pdf'  # Replace with your PDF file path
    analyze_pdf(file_path)
