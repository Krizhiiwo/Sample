import streamlit as st
import tempfile
import docx
from io import BytesIO
def extract_text_from_docx(file):
    doc_text = ""
    if file is not None:
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = f"{temp_dir}/uploaded_file.docx"
            # Save the uploaded file within the temporary directory
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(file.read())
            # Extract text from the temporary file
            doc = docx.Document(temp_file_path)
            for para in doc.paragraphs:
                doc_text += para.text + "\n"
    return doc_text
# Create a Streamlit app
st.title("Doc Text Extractor")
# File uploader for DOCX files
uploaded_file = st.file_uploader("Upload a Doc file", type=["docx"])
# Display DOCX contents if a file is uploaded
if uploaded_file is not None:
    doc_contents = extract_text_from_docx(uploaded_file)
    st.header("DOCX Contents:")
    st.text(doc_contents)