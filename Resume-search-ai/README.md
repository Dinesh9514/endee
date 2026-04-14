
AI Resume Search

Overview

AI Resume Search is a simple Artificial Intelligence project that demonstrates how vector search can be used to find relevant resumes based on a user query. The system converts resume text into vector embeddings and stores them in a FAISS vector database. When a query is entered, the system compares the query embedding with stored embeddings to find the most relevant resumes.

This project is designed to showcase the basic concept of semantic search using modern AI techniques.

---

Features

- Convert resumes into vector embeddings using Sentence Transformers
- Store embeddings in a FAISS vector database
- Perform semantic search on resumes
- Retrieve the most relevant resumes based on a query
- Fast similarity search using vector distance
- Simple and beginner-friendly implementation

---

Project Structure

resume-search-ai/
│
├── app.py
├── requirements.txt
├── README.md
└── demo.png

File Description

- app.py – Main program that generates embeddings and performs the search
- requirements.txt – Contains the required Python libraries
- README.md – Documentation of the project
- demo.png – Screenshot showing example output

---

Technologies Used

- Python
- Sentence Transformers
- FAISS (Facebook AI Similarity Search)
- NumPy

These tools help convert text into embeddings and perform efficient similarity search.

---

Installation

Clone the repository and move into the project folder.

git clone https://github.com/yourusername/endee.git
cd endee/resume-search-ai

Install dependencies:

pip install -r requirements.txt

---

How to Run

Run the main Python script:

python app.py

Example Query:

AI Engineer

Example Output:

Top results:
Python developer with AI experience
Machine learning engineer

---

How Vector Search Works

1. Resume text is converted into vector embeddings using Sentence Transformers.
2. These embeddings represent semantic meaning of the text.
3. The embeddings are stored in a FAISS vector index.
4. When a query is entered, it is also converted into an embedding.
5. FAISS calculates similarity between the query vector and stored vectors.
6. The most similar resumes are returned as search results.

This approach allows the system to find semantically similar resumes instead of relying only on keyword matching.

---

Example Use Cases

- Resume filtering for recruiters
- AI-based candidate search
- Semantic document search
- Knowledge base retrieval systems

---

Future Improvements

- Add support for multiple resume files
- Build a simple web interface
- Add PDF resume parsing
- Improve ranking with advanced embedding models
- Deploy as a web application

---

Demo

Example output screenshot:

(Add screenshot here)

---

Conclusion

This project demonstrates the fundamental concept of AI-powered semantic search using vector embeddings and FAISS. It provides a simple introduction to how modern AI systems retrieve information based on meaning rather than exact keyword matches.

---

Author

Dinesh S
Computer Science Engineering Student
 