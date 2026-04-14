

🚀 AI Resume Search using Vector Embeddings

📌 Project Overview

This project demonstrates a simple AI-powered resume search system using vector embeddings and similarity search.
The system converts resumes into numerical vectors and stores them in a vector index. When a user enters a query (for example, "AI Engineer"), the system finds the most relevant resumes using semantic similarity.

This project showcases the core concept used in modern AI search systems such as semantic search, recommendation systems, and retrieval-augmented AI.






🎯 Features

Convert text data into vector embeddings

Store embeddings in a vector database

Perform semantic similarity search

Retrieve the most relevant results based on meaning instead of keywords

Simple and lightweight implementation using Python







🧠 Vector Search Concept

Traditional search relies on keyword matching, which often misses context.

This project uses vector embeddings where:

1. Text documents are converted into numerical vectors.


2. These vectors represent semantic meaning.


3. Similar texts produce vectors that are close in vector space.


4. A vector search index retrieves the nearest vectors for a given query.



This allows the system to find semantically similar results even if exact keywords are not present.

Example:

Query:

AI Engineer

Result:

Python developer with machine learning experience

Even though the words are different, the meaning is similar, so it gets retrieved.







🛠️ Technologies Used

Python

Sentence Transformers

FAISS (Facebook AI Similarity Search)

NumPy







📂 Project Structure

endee/
   ai-resume-search/
       app.py
       requirements.txt
       README.md







⚙️ Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/endee.git

Navigate to the project folder:

cd endee/ai-resume-search

Install dependencies:

pip install -r requirements.txt







▶️ How to Run

Run the application:

python app.py

Example Output:

Top results:
Python developer with AI experience
Machine learning engineer







📸 Demo Output

Example result of semantic search:

Query: AI Engineer

Top Results:
1. Python developer with AI experience
2. Machine learning engineer

(Add a screenshot here if available)







🚀 Future Improvements

Add support for real resume datasets

Build a web interface for searching resumes

Store vectors in a scalable vector database

Add document upload support

Improve ranking and filtering







📚 Learning Outcome

Through this project, I learned:

Fundamentals of vector embeddings

How semantic search systems work

Using FAISS for vector similarity search

Building a simple AI-powered search application in Python






📌 Submission

This project was created as part of the Endee AI Internship assignment and demonstrates the implementation of vector search concepts in a practical application.

