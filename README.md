# QA-RAG: Exploring LLM Reliance on External Knowledge 

Some text about the study ...  Abstract / link to paper / ... Overview
## Overview
Llama
RAG


**Table of Contents**

- Requirements
- Dataset
- Workflow
   - Inference
- Project Structure


## Getting Started

### Prerequisites

- Get access to Language Model (Llama model at https://llama.meta.com/llama-downloads/)
- Relative API key(s) (HuggingFace API key or other platforms to access ML models, e.g. Replicate)
- Python 3.11 or higher
  
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
