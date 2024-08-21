AGENDA: WE ARE HERE USING LLAMA3 LOCALLY VIA OLLAMA. FOCUS IS HERE HOW TO USE OLLAMA and LLAMA3 MODEL.

Step 1: Download and Install Ollama
Start by visiting Ollama.com to download the Ollama application. Once downloaded, follow the installation steps for your operating system. To ensure it's installed correctly, open your terminal and run:
Bash: ollama

Step 2: Download LLaMA 3
Ollama provides various models, but for this guide, we'll focus on the Llama 3 model with 8 billion parameters. Note that larger models require more powerful hardware. To get started, download the Llama 3 model by running:
Bash: ollama pull llama3:8b

Test the model by running: ollama run llama3

Step 3: Set Up Your Python Project, create the virtual environment on your IDE and run:
--Create a virtual environment: python3 -m venv newbot
--Activate it: source newbot/bin/activate
--Install libraries: pip install langchain langchain-ollama

Step 4: Create test.py python file, initialize and invoke the model with a simple prompt:
from langchain_ollama.llms import OllamaLLM
mymodel = OllamaLLM(model="llama3")
outputvariable = mymodel.invoke(input="how many gold medals india won in asian games 2022")
print(outputvariable)

Run the file: Python test.py
