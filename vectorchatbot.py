from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# Initialize the model
model = OllamaLLM(model="llama3")

# Create a prompt template:
template = """
{context}

You may use the above context to answer following question
Question: {question}
Answer:
"""

oembed = OllamaEmbeddings(model="llama3")
db = Chroma(embedding_function=oembed)

# chain the prompt with the model
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Define a main function to handle chat
def handle_chat():
    # Welcome message
    print("Welcome to the AI Chatbot. Type 'bye' to quit.")

    # Loop to continuously interact with the chatbot
    id = 1
    while True:
        user_input = input("You: ")

        # Stop condition i.e. when user says "bye"
        if user_input.lower() == "bye":
            break

        context = ""
        results = db.similarity_search(user_input, k=2)
        for res in results:
            context += res.page_content
            
        # Invoke the chain (prompt | model) with the given context and question
        result = chain.invoke(input= {
                    "context": context,
                    "question": user_input
                })
        
        document = Document(
            page_content= f"User: {user_input}\nAI: {result}\n"
        )

        db.add_documents(documents = [document]);

        print(f"Bot: {result}")

if __name__ ==  "__main__":
    handle_chat()