# QA-RAG: Exploring LLM Reliance on External Knowledge 

- This repo contains code and resources for the paper "QA-RAG: Exploring LLM Reliance on External Knowledge".

- The bemchmark dataset can be found and downloaded at [TriviaQA website][triviaqa-website].  

For suggestions and comments please contact Aigerim Mansurova (<222215@astanait.edu.kz).



## Overview
Llama
RAG


![alt text](https://github.com/Tbinma/Exploring-LLM-Reliance-on-External-Knowledge/blob/main/Workflow.png?raw=true)
The overall system architecture is depicted in figure above, detailing the sequential steps as follows:
1.	The query is forwarded to the embedding model for encoding into an embedded query vector.
2.	The embedded query vector is then transmitted to a vector database.
3.	The retriever algorithm dictates the retrieval of the top-k pertinent segments from the database.
4.	Subsequently, both the query text and the retrieved segments are forwarded to the Generator.
5.	LLM generates output that must be relevant and contextually connected to the origi-nal query and the information retrieved from the database.


## Getting Started

TriviaQA dataset Source: https://www.kaggle.com/datasets/vissarionmoutafis/triviaqatosquad?resource=download 

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
llm eval.py
```
Testbeds can be found in folder



 
!!! chabfe at the end
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
