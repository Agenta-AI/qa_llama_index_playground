# Question Answering RAG using LlamaIndex in agenta


This templates is a question answering application with a RAG architecture using LlamaIndex, openAI. It provides a playground to experiment with different prompts and parameters in LlamaIndex and evaluate the results.
It runs with agenta. [Agenta](https://github.com/agenta-ai/agenta) is an open-source LLMOps 
platform that allows you to 1) create a playground from the code of any LLM app to quickly experiment, version, and collaborate in your team 2) evaluate LLM applications, and 3) deploy applications easily. 

## How to use
### 0. Prerequisites
-  Install the agenta CLI
```bash
pip install agenta
```
- Either create an account in [agenta cloud](https://cloud.agenta.ai/) or 
[self-host agenta](/self-host/host-locally)

### 1. Clone the repository

```bash
git clone https://github.com/Agenta-AI/qa_llama_index_playground.git
```

### 2. Initialize the project

```bash
cd qa_llama_index_playground
agenta init
```

### 3. Setup your openAI API key
Create a .env file by copying the .env.example file and add your openAI 
API key to it.
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

### 4. Deploy the application to agenta

```bash
agenta variant serve app.py
```

### 5. Experiment with the prompts in a playground and evaluate different variants in agenta

https://github.com/Agenta-AI/job_extractor_template/assets/4510758/30271188-8d46-4d02-8207-ddb60ad0e284

