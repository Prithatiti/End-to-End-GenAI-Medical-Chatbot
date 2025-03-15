from flask import Flask, render_template, jsonify, request
from source.utility import download_hugging_face_embedding
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain  # Creates a retrieval-based chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from source.prompt import *
import os


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

embeddings = download_hugging_face_embedding()


index_name = "aimedibot"

docSearch = PineconeVectorStore.from_existing_index(
    index_name = index_name,  # Use the created index
    embedding = embeddings  # Embedding model used for vectorizing queries/documents
)


retriver = docSearch.as_retriever(  # Convert the Pinecone vector store into a retriever
    search_type = "similarity",       # Use similarity-based search to find the closest matches
    search_kwargs = {'k': 3}          # Retrieve the top 3 most similar results
)


# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash", 
    google_api_key = GOOGLE_API_KEY
)


# Create a structured prompt template using ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),  # The system message containing AI instructions
        ("human", "{input}"),  # Placeholder for the user input/question
    ]
)


# Creates a chain that takes the LLM (language model) and the prompt
# This chain structures the retrieved documents into a clear, usable format for the LLM to generate an answer
question_answer_chain = create_stuff_documents_chain(llm, prompt)


# Creates a Retrieval-Augmented Generation (RAG) chain
# This combines the retriever (which fetches relevant documents) with the question-answer chain
# It ensures the LLM gets the right context before generating a response
rag_chain = create_retrieval_chain(retriver, question_answer_chain)



@app.route("/")
def index():
    return render_template(
        "chatbot.html",
        welcome_message = "Hi there! How can I assist you today?"
    )


@app.route("/get", methods = ["GET", "POST"])
def chat():
    message = request.form["msg"]
    input = message
    print(input)

    response = rag_chain.invoke({"input" : message})
    print(f"Response : {response["answer"]}")

    return str(response["answer"])


if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
        port = 8080,
        debug = True
    )