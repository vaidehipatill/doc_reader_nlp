# Document Insight Assistant

The **Document Insight Assistant** is a web application that allows users to upload academic PDFs and interact with them using natural language queries. Powered by OpenAI’s language models and vector-based retrieval, this tool is designed to help students and researchers extract relevant information from large documents efficiently.

## Features

* Upload and process PDF documents
* Ask questions and receive context-aware answers from the document
* Vector-based document retrieval using FAISS and OpenAI embeddings
* Session-based chat memory to maintain context
* Option to download chat history
* Clean and modular code structure for easy extension

## Installation

1. **Clone the repository**

   ```
   git clone https://github.com/yourusername/document-insight-assistant.git
   cd document-insight-assistant
   ```

2. **Install required packages**

   ```
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API Key**
   Get your API key from [OpenAI](https://platform.openai.com/account/api-keys) and set it as an environment variable:

   ```
   export OPENAI_API_KEY=your-api-key-here
   ```

   Alternatively, the key can be entered manually in the application sidebar when running.

## Usage

1. Run the application using Streamlit:

   ```
   streamlit run app.py
   ```

2. Open your browser and navigate to:

   ```
   http://localhost:8501
   ```

3. Upload a PDF, enter your API key if prompted, and start asking questions based on the uploaded document.

## Project Structure

```
├── app.py          # Streamlit app and UI logic
├── chat.py         # Chat response generation and vector search
├── utils.py        # PDF processing and text chunking utilities
├── requirements.txt
```

## Technologies Used

* Python
* Streamlit
* OpenAI API
* FAISS (Facebook AI Similarity Search)
* PyPDFLoader

## Contributions

This project was developed as an academic assignment focusing on improving baseline document-based question-answering systems. Key contributions include:

* Replacing basic retrieval with FAISS vector search
* Modular design splitting application logic into separate files
* Building a session-based memory for chat interaction
* Implementing document transcript download functionality

