

# File Reader App

A Streamlit-based application that allows users to upload and read different file types, including `.docx`, `.xlsx`, `.pdf`, and `.txt`. This app provides a simple and intuitive interface for previewing the contents of these files directly in the browser.

---

## Features

- **Read `.docx` files**: Display the text content of Microsoft Word documents.
- **Read `.xlsx` files**: Preview Excel spreadsheets in a tabular format.
- **Read `.pdf` files**: Extract and display the text from PDF documents.
- **Read `.txt` files**: Show the content of plain text files.

---

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Clone the Repository

```bash
git clone https://github.com/yourusername/file-reader-app.git
cd file-reader-app
```

### Install Dependencies

Install the required Python libraries:

```bash
pip install streamlit python-docx pandas PyPDF2 openpyxl
```

---

## Usage

### Run the Application

Start the Streamlit app by running the following command:

```bash
streamlit run app.py
```

### Upload Files

1. Open the app in your web browser (Streamlit will provide a local URL after running the above command).
2. Use the sidebar to upload files of type `.docx`, `.xlsx`, `.pdf`, or `.txt`.
3. View the content of the uploaded file in the main area of the app.

---

## File Handling Details

### DOCX Files
The app extracts and displays the text content of Word documents using the `python-docx` library.

### XLSX Files
The app reads and displays Excel files in a table format using the `pandas` library. It supports `.xlsx` files created in Microsoft Excel or similar software.

### PDF Files
The app extracts text from PDF files using the `PyPDF2` library.

### TXT Files
The app reads and displays the content of plain text files.

---

## Dependencies

- [Streamlit](https://streamlit.io/) - Web application framework for Python.
- [python-docx](https://pypi.org/project/python-docx/) - For reading `.docx` files.
- [pandas](https://pandas.pydata.org/) - For handling `.xlsx` files.
- [PyPDF2](https://pypi.org/project/PyPDF2/) - For reading `.pdf` files.
- [openpyxl](https://pypi.org/project/openpyxl/) - Required for reading Excel files.

---

## Screenshots

### Upload File
![Upload File Screenshot](screenshots/upload_file.png)

### Display Content
![Display Content Screenshot](screenshots/display_content.png)

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or suggestions, feel free to reach out:

- **Email**: srphysics04@gmail.com
- **GitHub**: [sugeng-riyanto](https://github.com/sugeng-riyanto)
