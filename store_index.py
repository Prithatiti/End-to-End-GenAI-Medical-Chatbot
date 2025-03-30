from source.utility import load_pdf_file, text_splitter, download_hugging_face_embedding
import os
# import pinecone
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore



load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


extracted_data = load_pdf_file(data = 'Data/')
text_chunks = text_splitter(extracted_data)
embeddings = download_hugging_face_embedding()


# Create a Pinecone client instance
pc = Pinecone(api_key = PINECONE_API_KEY)

index_name = "aimedibot"

# Create an index
pc.create_index(
    name = index_name,
    dimension = 384,  # Replace with your model's dimensions
    metric = "cosine",  # Replace with your preferred metric

    spec = ServerlessSpec(
        cloud = "aws",
        region = "us-east-1"
    )
)


# Embed each chunk and upsert the embeddings into your pinecone index
docSearch = PineconeVectorStore.from_documents(
    documents = text_chunks,
    index_name = index_name,
    embedding = embeddings
)