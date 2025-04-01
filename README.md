# End to End GenAI Medical Chatbot

## 🚀 Overview
The **Medical Chatbot** is an AI-powered assistant designed to provide medical information and answer queries. This guide walks you through setting up and running the chatbot on your local machine.

---

## 🛠️ Installation and Setup Guide:~

### **Step 1: Clone the Repository**
First, clone the project repository from GitHub:
```bash
# Replace with the actual GitHub repository link
git clone https://github.com/YOUR-REPO/MEDICAL-CHATBOT.git
cd MEDICAL-CHATBOT
```

---

### **Step 2: Set Up a Conda Environment**
Create and activate a new Conda environment:
```bash
conda create -n medibot python=3.12 -y
conda activate medibot
```

---

### **Step 3: Install Dependencies**
Install all required Python packages:
```bash
pip install -r requirements.txt
```

---

### **Step 4: Configure API Keys**
Create a `.env` file in the root directory and add the necessary API credentials:
```ini
PINECONE_API_KEY = "your_pinecone_api_key_here"
GOOGLE_API_KEY = "your_google_api_key_here"
```
Replace `your_pinecone_api_key_here` and `your_google_api_key_here` with your actual credentials.

---

### **Step 5: Store Embeddings in Pinecone**
Run the following command to store embeddings in Pinecone:
```bash
python store_index.py
```

---

### **Step 6: Run the Chatbot**
Start the chatbot application:
```bash
python app.py
```

---

### **Step 7: Access the Chatbot**
Once the chatbot is running, open your browser and go to:
```
localhost:8080
```
This will open the chatbot interface on your local machine.

---

## 🎯 Summary
✅ Clone the repository  
✅ Set up a Conda environment  
✅ Install dependencies  
✅ Configure API keys  
✅ Store embeddings in Pinecone  
✅ Run the chatbot  
✅ Open it in the browser  

Now, you’re all set to use the **Medical Chatbot**! 🚀

---

## 🛠 Tech Stack Used
- Python  
- LangChain  
- Flask  
- GPT  
- Pinecone
