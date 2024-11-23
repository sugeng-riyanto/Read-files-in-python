import streamlit as st
import docx
import pandas as pd
import PyPDF2

# Function to read DOCX files
def read_docx(file):
    doc = docx.Document(file)
    content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return content

# Function to read XLSX files
def read_xlsx(file):
    try:
        data = pd.read_excel(file)
        return data
    except Exception as e:
        return f"Error reading Excel file: {e}"

# Function to read PDF files
def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    content = ""
    for page in pdf_reader.pages:
        content += page.extract_text()
    return content

# Function to read TXT files
def read_txt(file):
    return file.read().decode("utf-8")

# Streamlit app
def main():
    st.title("File Reader App")
    st.sidebar.header("Upload Your File")
    
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["docx", "xlsx", "pdf", "txt"])
    
    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1]
        
        if file_type == "docx":
            st.subheader("Content of the DOCX File")
            content = read_docx(uploaded_file)
            st.text_area("File Content", content, height=300)
        
        elif file_type == "xlsx":
            st.subheader("Content of the XLSX File")
            content = read_xlsx(uploaded_file)
            if isinstance(content, pd.DataFrame):
                st.dataframe(content)
            else:
                st.error(content)
        
        elif file_type == "pdf":
            st.subheader("Content of the PDF File")
            content = read_pdf(uploaded_file)
            st.text_area("File Content", content, height=300)
        
        elif file_type == "txt":
            st.subheader("Content of the TXT File")
            content = read_txt(uploaded_file)
            st.text_area("File Content", content, height=300)
        
        else:
            st.error("Unsupported file type!")

if __name__ == "__main__":
    main()
