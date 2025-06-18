# 📄 Resume RAG Q&A App

An interactive Streamlit app that lets you ask questions about your resume using Retrieval-Augmented Generation (RAG). It uses OpenAI for embeddings and chat responses, and Pinecone for vector storage.



## 🔍 Features

- Upload and process multiple PDF resumes
- Ask natural language questions about resume content
- Generate customized cover letters
- Match resume to a job description and calculate similarity
- Export Q&A chat history as `.txt`, `.csv`, or `.docx`


## ⚙️ Tech Stack

- **Frontend**: Streamlit
- **LLM**: OpenAI GPT-4o
- **Embeddings**: OpenAI `text-embedding-3-small`
- **Vector Database**: Pinecone
- **PDF Parsing**: `pdfminer.six`
- **Text Export**: `python-docx`



## 🗂️ Project Structure

```text
resume-rag-qna/
├── streamlitapp.py
├── requirements.txt
├── README.md
├── .gitignore
├── utils/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embedder.py
│   ├── pinecone_store.py
```



## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Payal2000/Resume-RAG-.git
cd Resume-RAG-
```

### 2. Set up virtual environment (optional)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your secrets

Set the following environment variables or add them to Streamlit secrets:

- `OPENAI_API_KEY`
- `PINECONE_API_KEY`
- `PINECONE_ENVIRONMENT`
- `PINECONE_INDEX_NAME`



## 🧪 Run Locally

```bash
streamlit run streamlitapp.py
```



## ☁️ Deploy to Streamlit Cloud

1. Push your repo to GitHub  
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)  
3. Click **"New app"** and select your repository  
4. Add all secrets in the app’s **Settings**  
5. Click **"Deploy"**



## 📎 Export Options

Download chat history in:

- `.txt`
- `.csv`
- `.docx`



## 📬 Contact

- **Payal Nagaonkar**  
- 📧 [nagaonkar.p@northeastern.edu](mailto:nagaonkar.p@northeastern.edu)  
- 🔗 [LinkedIn](https://www.linkedin.com/in/payal-sanjay-nagaonkar-76b733188/)



## 🪪 License

This project is licensed under the MIT License.
