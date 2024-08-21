
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate

# initialize the model
model = OllamaLLM(model="llama3")

# create a prompt template:
template = """
{context}

You may use the above context to answer following question
Question: {question}
Answer:
"""

# chain the prompt with the model
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# main function to handle chat
def handle_chat():
    # To store chat history
    history = "" 

    # welcome message
    print("Welcome to the AI Chatbot. Type 'bye' to quit.")
    
    # loop to continuously interact with the chatbot
    while True:
        user_input = input("You: ")

        # stop condition i.e. when user says "bye"
        if user_input.lower() == "bye":
            break
       
        # invoke the chain i.e. prompt | model
        result = chain.invoke(input= {
                    "context": history,
                    "question": user_input
                })

        print(f"Bot: {result}")
        
        history += f"User: {user_input}\nBot: {result}\n"

if __name__ == "__main__":
    handle_chat()

#note: it was a simple chatbot we developed here, didn't use customize data or vectorized it.