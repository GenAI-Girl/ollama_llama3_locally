from langchain_ollama.llms import OllamaLLM

# initialize the model
model = OllamaLLM(model="llama3")

# invoke the model with a simple prompt
result = model.invoke(input="how many gold medals india won in asian games 2022?")

print(result)

