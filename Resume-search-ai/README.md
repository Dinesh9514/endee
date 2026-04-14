# 🤖 AI Resume Search


## 📌 Overview

**AI Resume Search** is a simple Artificial Intelligence project that demonstrates how **vector search** can be used to find relevant resumes based on a user query.

The system converts resume text into **vector embeddings** and stores them in a **FAISS vector database**. When a query is entered, it compares embeddings to retrieve the most relevant resumes.

✨ This project showcases the concept of **semantic search**, where results are based on meaning rather than exact keywords.

---

## 🚀 Features

* 🔹 Convert resumes into vector embeddings using Sentence Transformers
* 🔹 Store embeddings in a FAISS vector database
* 🔹 Perform semantic search on resumes
* 🔹 Retrieve the most relevant resumes
* 🔹 ⚡ Fast similarity search
* 🔹 🧠 Beginner-friendly implementation

---

## 📂 Project Structure

```
resume-search-ai/
│
├── app.py
├── requirements.txt
├── README.md
```

---

## 📄 File Description

* 🧩 **app.py** – Main program for embeddings and search
* 📦 **requirements.txt** – Required libraries
* 📘 **README.md** – Documentation

---

## 🛠️ Technologies Used

* 🐍 Python
* 🤖 Sentence Transformers
* 🔍 FAISS (Facebook AI Similarity Search)
* 📊 NumPy

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/endee.git
cd endee/resume-search-ai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python app.py
```

---

## 🔎 Example

### 💡 Query

```
AI Engineer
```

### 📊 Output

```
Top results:
- Python Developer with AI experience
- Machine Learning Engineer
```

---

## 🧠 How Vector Search Works

1. 📄 Convert resume text into embeddings
2. 🔢 Capture semantic meaning
3. 💾 Store in FAISS index
4. 🔍 Convert query into embedding
5. ⚖️ Compare similarity
6. 🏆 Return best matches

✨ This approach enables **context-aware search**, not just keyword matching.

---

## 💼 Use Cases

* 👨‍💼 Resume filtering for recruiters
* 🤖 AI-based candidate search
* 📚 Semantic document search
* 🧾 Knowledge base retrieval

---

## 🔮 Future Improvements

* 📂 Support multiple resumes
* 🌐 Build a web interface
* 📄 Add PDF parsing
* 📈 Improve ranking models
* 🚀 Deploy as a web app

---

## 🖼️ Demo

📸 Add your screenshot here:
![Demo](demo.png)

---

## 📌 Conclusion

This project demonstrates the fundamentals of **AI-powered semantic search** using vector embeddings and FAISS.

It helps understand how modern AI systems retrieve information based on **meaning instead of exact words**.

---

## 👨‍💻 Author

**Dinesh S**
🎓 Computer Science Engineering Student

---

⭐ *If you like this project, don't forget to star the repository!*
