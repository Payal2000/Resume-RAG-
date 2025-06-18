from pdfminer.high_level import extract_text
import tempfile

def extract_resume_text(uploaded_file):
    # Write the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Extract text from the temporary file
    return extract_text(tmp_path)
