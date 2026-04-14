from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

docs = [
    "Python developer with AI experience",
    "Java backend developer",
    "Machine learning engineer",
    "Frontend developer React"
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(docs)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

query = "AI engineer"

query_vector = model.encode([query])

distances, indices = index.search(query_vector, k=2)

print("Top results:")
for i in indices[0]:
    print(docs[i])
