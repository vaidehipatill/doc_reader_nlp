# Document Insight Assistant

The Document Insight Assistant is a web application that allows users to upload academic/business/informational PDFs and interact with them using natural language queries. Powered by OpenAI’s language models and vector-based retrieval, this tool is designed to help students and researchers extract relevant information from large documents efficiently.

## Links

GitHub: https://github.com/vaidehipatill/doc_reader_nlp
YouTube: https://www.youtube.com/watch?v=MWHp99dzJZc

## Features

* Upload and process PDF documents
* Ask questions and receive context-aware answers from the document
* Vector-based document retrieval using FAISS and OpenAI embeddings
* Session-based chat memory to maintain context
* Option to download chat history
* Clean and modular code structure for easy extension


## About This Project

This project showcases the integration of modern language models with efficient retrieval techniques, packaged in an interactive web app.

Key innovations and contributions include:
* Upgraded Retrieval: Replaced basic keyword search with FAISS-based vector similarity search for more accurate and context-aware retrieval.
* Modular Architecture: Designed the app using a clean, modular structure with separate components for PDF processing, vector storage, GPT interaction, and the Streamlit interface.
* Session-based Chat Memory: Implemented chat memory within user sessions, enabling multi-turn conversations with consistent context.
* Downloadable Transcripts: Added a feature to download chat transcripts of document conversations for future reference.


## Structure

- Streamlit (UI)  
- OpenAI API (chat completion)  
- FAISS / Chroma (vector storage)  
- PDF processing (via PyMuPDF)  


├── app.py              # Main Streamlit app
├── chatbot.py          # GPT call logic
├── pdf_processor.py    # Extracts text from uploaded PDFs
├── vector_store.py     # Stores and retrieves document chunks via vector search
├── .env                # Your secret OpenAI API key
├── requirements.txt    # Python dependencies
└── README.md           # This file


## Installation

1. Clone the repository
   
	git clone https://github.com/vaidehipatill/_______________.git
	cd document-insight-assistant
   

2. Set up a virtual environment (recommended)

	python -m venv .venv
	source .venv/bin/activate   # For Mac/Linux
	# OR
	.venv\Scripts\activate      # For Windows


3. Install required packages
   
   	pip install -r requirements.txt


4. Set up OpenAI API Key
   
	Create a file named `.env` in the root directory and add your key:

	OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx


## Usage

1. Run the application using Streamlit:
   
   streamlit run app.py


2. Open your browser and navigate to:
   
   http://localhost:8501


3. Upload a PDF, enter your API key if prompted, and start asking questions based on the uploaded document.


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


## Project By:
Vaidehi Mahesh Patil
CS 6320.001
6th May 2025.
