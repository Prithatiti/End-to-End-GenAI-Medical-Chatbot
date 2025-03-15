from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from huggingface_hub import hf_hub_download



# Extract the Data from The PDF file

def load_pdf_file(data):
    loader = DirectoryLoader(
        data,
        glob = "*.pdf",
        loader_cls = PyPDFLoader
    )

    documents = loader.load()

    return documents


# Split the Data into Text Chunks

def text_splitter(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 20
    )

    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks


# Download the Embeddings from Hugging Face

def download_hugging_face_embedding():
    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings