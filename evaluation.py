import numpy as np
from sklearn.metrics import ndcg_score
from langchain.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

# Load Pinecone Retriever (Modify as per your setup)
def load_retriever():
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    vector_store = Pinecone.from_existing_index(index_name="your_pinecone_index", embedding=embeddings)
    return vector_store.as_retriever()

# Define queries and expected ground truth
queries = [
    "What are the symptoms of diabetes?",
    "How to treat hypertension?",
    "What are the side effects of ibuprofen?"
]

ground_truths = [
    "Diabetes symptoms include increased thirst, frequent urination, and fatigue.",
    "Hypertension is treated with lifestyle changes and medications like ACE inhibitors.",
    "Common side effects of ibuprofen are nausea, dizziness, and stomach pain."
]

# Evaluate Retrieval Performance
def evaluate_retrieval(retriever, queries, ground_truths, k=5):
    precision_scores = []
    recall_scores = []
    ndcg_scores = []

    for query, truth in zip(queries, ground_truths):
        retrieved_docs = retriever.get_relevant_documents(query, k=k)
        retrieved_texts = [doc.page_content for doc in retrieved_docs]

        # Precision@K Calculation
        relevant_retrieved = sum([1 for doc in retrieved_texts if truth.lower() in doc.lower()])
        precision = relevant_retrieved / k
        precision_scores.append(precision)

        # Recall@K Calculation (Assuming all relevant docs are in corpus)
        recall = relevant_retrieved / 1  # Assuming 1 perfect match exists
        recall_scores.append(recall)

        # NDCG Calculation
        relevance = np.array([1 if truth.lower() in doc.lower() else 0 for doc in retrieved_texts])
        ideal_relevance = sorted(relevance, reverse=True)  # Ideal sorted order
        ndcg = ndcg_score([ideal_relevance], [relevance])
        ndcg_scores.append(ndcg)

    # Print Metrics
    print("\n📊 **Retrieval Evaluation Metrics**")
    print(f"🔹 Average Precision@{k}: {np.mean(precision_scores):.4f}")
    print(f"🔹 Average Recall@{k}: {np.mean(recall_scores):.4f}")
    print(f"🔹 Average NDCG@{k}: {np.mean(ndcg_scores):.4f}")

if __name__ == "__main__":
    retriever = load_retriever()
    evaluate_retrieval(retriever, queries, ground_truths)