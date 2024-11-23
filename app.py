import streamlit as st  # Importing Streamlit library for building the web app
import docx  # Importing the python-docx library to work with DOCX files
import pandas as pd  # Importing Pandas for data manipulation and reading Excel files
import PyPDF2  # Importing PyPDF2 for reading PDF files

# Function to read DOCX files
def read_docx(file):
    # Open the DOCX file using docx.Document
    doc = docx.Document(file)
    # Extract all the paragraphs' text and join them with a newline
    content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return content  # Return the content as a single string

# Function to read XLSX (Excel) files
def read_xlsx(file):
    try:
        # Attempt to read the Excel file into a Pandas DataFrame
        data = pd.read_excel(file)
        return data  # Return the DataFrame if successful
    except Exception as e:
        # Return an error message if reading the file fails
        return f"Error reading Excel file: {e}"

# Function to read PDF files
def read_pdf(file):
    # Open the PDF file using PyPDF2
    pdf_reader = PyPDF2.PdfReader(file)
    content = ""  # Initialize an empty string to hold the PDF content
    for page in pdf_reader.pages:  # Iterate through each page in the PDF
        content += page.extract_text()  # Extract and append the text of the current page
    return content  # Return the complete content as a string

# Function to read TXT files
def read_txt(file):
    # Decode the uploaded file's content to a string (assuming UTF-8 encoding)
    return file.read().decode("utf-8")

# Main function to define the Streamlit app
def main():
    st.title("File Reader App")  # Set the title of the web app
    st.sidebar.header("Upload Your File")  # Add a header to the sidebar for file upload
    
    # Create a file uploader widget in the sidebar to accept specific file types
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["docx", "xlsx", "pdf", "txt"])
    
    if uploaded_file is not None:  # Check if a file has been uploaded
        # Get the file extension to determine the type of the uploaded file
        file_type = uploaded_file.name.split(".")[-1]
        
        # Handle DOCX files
        if file_type == "docx":
            st.subheader("Content of the DOCX File")  # Add a subheader for clarity
            content = read_docx(uploaded_file)  # Read the content of the DOCX file
            # Display the content in a text area widget
            st.text_area("File Content", content, height=300)
        
        # Handle XLSX (Excel) files
        elif file_type == "xlsx":
            st.subheader("Content of the XLSX File")  # Add a subheader for clarity
            content = read_xlsx(uploaded_file)  # Read the content of the Excel file
            if isinstance(content, pd.DataFrame):  # Check if the content is a DataFrame
                st.dataframe(content)  # Display the DataFrame as an interactive table
            else:
                st.error(content)  # Display an error message if the file couldn't be read
        
        # Handle PDF files
        elif file_type == "pdf":
            st.subheader("Content of the PDF File")  # Add a subheader for clarity
            content = read_pdf(uploaded_file)  # Read the content of the PDF file
            # Display the content in a text area widget
            st.text_area("File Content", content, height=300)
        
        # Handle TXT files
        elif file_type == "txt":
            st.subheader("Content of the TXT File")  # Add a subheader for clarity
            content = read_txt(uploaded_file)  # Read the content of the TXT file
            # Display the content in a text area widget
            st.text_area("File Content", content, height=300)
        
        # Handle unsupported file types
        else:
            st.error("Unsupported file type!")  # Show an error message if the file type is not handled

# Check if the script is run directly
if __name__ == "__main__":
    main()  # Call the main function to start the app
