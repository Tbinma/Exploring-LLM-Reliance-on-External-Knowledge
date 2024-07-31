# QA-RAG: Exploring LLM Reliance on External Knowledge 

Some text about the study ...  Abstract / link to paper / ... Overview
## Overview
Llama
RAG
Figure 1. 

## Getting Started

### Prerequisites

- Get access to Language Model (Llama model at https://llama.meta.com/llama-downloads/)
- Relative API key(s) (HuggingFace API key or other platforms to access ML models, e.g. Replicate, OpenAI)

  
**Requirements**
Ensure that the following dependencies are installed:
- Hugging Face Transformers library
- LangChain community library
- Python 3.11+
- PyTorch
- bitsandbytes
- ChromaDB vector storage library
- Additional dependencies if required by your environment.

### Installation
1. Install dependencies.
You can install dependencies using :
```
pip install -r requirements.txt
```

2. Create the Chroma DB (external knowledge base):
```
python vector_database.py
```
 !!!!! CHANGEE FOR HF  

3. Load the base Llama model 
llm = 


4. Create a question/SYSTEM prompt using the provided utility? functions.?

line to change the prompt


5. Test run to query the Chroma DB?
answer without llm, just 
response with sim.search


6. query to chroma with LLM answers 
   Test run to query the Chroma DB, the below command will return an output based on RAG and the selected model:
```
python query_data.py "Which role does Adam Goldberg plays?"
```
example and code is only with dense 

7. if you want to use hybrid use - code.py

8.  Evaluate the system answers using LLMs-as-judges:
```
streamlit run app.py
```

9. Testbeds can be found in folder


!!!
 --------------------------------
3. Setup [LLM, retriever] before being able to do inference:

 
   - Case 2: If you choose to do inference with replicate with our models locally, you'll need to have `REPLICATE_API_TOKEN` setup as an environment variable.

4. Test run to query the Chroma DB, the below command will return an output based on RAG and the selected model:
```
python query_data.py "Which role does Adam Goldberg plays?"
```

 --------------------------------
 

**Workflow**

 Inference

To use the trained Llama model for question answering, you can utilize the inference script. Here's how:

1. Load the pretrained Llama model (or train your own as described above).
2. Create a question prompt using the provided utility functions.
3. Generate responses to your questions using the Llama model.
4. Analyze and evaluate the responses as needed.



**Project Structure**

The project structure is organized as follows:

```
project-root/
  ├── README.md
  ├── main.py               # Training script (customize for your dataset)
  ├── eval.py               # Inference script for question answering
  ├── model.py              # Llama model definition and utilities
  ├── dataset.py            # Dataset loading and preprocessing
  └── requirements.txt      # List of Python dependencies
```
