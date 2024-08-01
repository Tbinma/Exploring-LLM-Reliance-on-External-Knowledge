# QA-RAG: Exploring LLM Reliance on External Knowledge 

- This repo contains code and resources for the paper "QA-RAG: Exploring LLM Reliance on External Knowledge".

- The benchmark dataset can be found and downloaded at [TriviaQA website][triviaqa-website].  

For suggestions and comments please contact Aigerim Mansurova (<222215@astanait.edu.kz).



## Overview

The overall system architecture is depicted in the figure, detailing the sequential steps as follows:

![alt text](https://github.com/Tbinma/Exploring-LLM-Reliance-on-External-Knowledge/blob/main/Workflow.png?raw=true)
1.	The query is forwarded to the embedding model for encoding into an embedded query vector.
2.	The embedded query vector is then transmitted to a vector database.
3.	The retriever algorithm dictates the retrieval of the top-k pertinent segments from the database.
4.	Subsequently, both the query text and the retrieved segments are forwarded to the Generator.
5.	LLM generates output that must be relevant and contextually connected to the origi-nal query and the information retrieved from the database.


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
vectordb = Chroma(
    embedding=embedding_model,
    persist_directory=persist_directory #path to directory for vector database
)
```

3. Load the base Llama model
Select and load the desired language model. Changing the model is straightforward; simply update the model_id to the desired model identifier.
 Your selected language model
```
model_id = "meta-llama/Llama-2-13b-hf"

```

4. Create a custom prompt as in custom prompt.py.

Example of weak prompt style:
```
prompt_template = """
Consider the following context when answering the question. Don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:
"""
```

5. Query the Chroma database and obtain answers using a RAG approach, leveraging a selected language model:
```
QnA = RetrievalQA.from_chain_type(
    llm=llm,                          
    chain_type="stuff",               
    retriever=retriever,              
    # chain_type_kwargs=chain_type_kwargs, # Optional: Custom prompt configuration
    return_source_documents=True      # Return source documents along with the answer
)

# Define the query
query = "Your query here"

# Execute the query
llm_response = QnA(query)
```
6.  Evaluate the system answers using LLMs-as-judges:
Refer to [documentation](https://github.com/explodinggradients/ragas)  to learn more.

Testbeds can be found in folder
```
testbeds
```


 
!!! change at the end
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



[triviaqa-website]: http://nlp.cs.washington.edu/triviaqa/

