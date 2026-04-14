
🤖 AI Resume Search
📌 Overview

AI Resume Search is a simple Artificial Intelligence project that demonstrates how vector search can be used to find relevant resumes based on a user query.

The system converts resume text into vector embeddings and stores them in a FAISS vector database. When a query is entered, it compares embeddings to retrieve the most relevant resumes.

✨ This project showcases the core concept of semantic search using modern AI techniques.

🚀 Features
🔹 Convert resumes into vector embeddings using Sentence Transformers
🔹 Store embeddings in a FAISS vector database
🔹 Perform semantic search on resumes
🔹 Retrieve the most relevant resumes based on a query
🔹 ⚡ Fast similarity search using vector distance
🔹 🧠 Beginner-friendly implementation
📂 Project Structure
resume-search-ai/
│
├── app.py
├── requirements.txt
├── README.md
└── demo.png
📄 File Description
🧩 app.py – Main program for generating embeddings and performing search
📦 requirements.txt – List of required Python libraries
📘 README.md – Project documentation
🖼️ demo.png – Example output screenshot
🛠️ Technologies Used
🐍 Python
🤖 Sentence Transformers
🔍 FAISS (Facebook AI Similarity Search)
📊 NumPy

These tools help convert text into embeddings and enable efficient similarity search.

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/endee.git
cd endee/resume-search-ai
2️⃣ Install Dependencies
pip install -r requirements.txt
▶️ How to Run
python app.py
🔎 Example
💡 Query:
AI Engineer
📊 Output:
Top results:
- Python Developer with AI experience
- Machine Learning Engineer
🧠 How Vector Search Works
📄 Resume text is converted into vector embeddings using Sentence Transformers
🔢 These embeddings capture the semantic meaning
💾 Stored in a FAISS vector index
🔍 Query is also converted into an embedding
⚖️ FAISS calculates similarity between vectors
🏆 Most relevant resumes are returned

✨ This method goes beyond keyword matching and understands context and meaning.

💼 Use Cases
👨‍💼 Resume filtering for recruiters
🤖 AI-based candidate search
📚 Semantic document search
🧾 Knowledge base retrieval systems
🔮 Future Improvements
📂 Support multiple resume files
🌐 Build a web interface
📄 Add PDF resume parsing
📈 Improve ranking with advanced models
🚀 Deploy as a web application
🖼️ Demo

📸 Example output screenshot:
(Add your demo.png here)

📌 Conclusion

This project demonstrates the fundamentals of AI-powered semantic search using vector embeddings and FAISS.

It provides a strong foundation for understanding how modern AI systems retrieve information based on meaning rather than exact keywords.

👨‍💻 Author

Dinesh S
🎓 Computer Science Engineering Student
 
