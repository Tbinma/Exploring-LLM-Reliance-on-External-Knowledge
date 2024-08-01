import torch
from torch import cuda, bfloat16
import transformers
from langchain.llms import HuggingFacePipeline
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
import argparse

def main(hf_auth, persist_directory, query):
    # Load embedding model
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2")

    # Load the existing vector database
    vectordb = Chroma(
        embedding=embedding_model,
        persist_directory=persist_directory
    )

    model_id = "meta-llama/Llama-2-13b-hf"

    device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'

    # Set quantization configuration to load large model with less GPU memory
    bnb_config = transformers.BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=bfloat16
    )

    model_config = transformers.AutoConfig.from_pretrained(
        model_id,
        use_auth_token=hf_auth
    )

    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_id,
        trust_remote_code=True,
        config=model_config,
        quantization_config=bnb_config,
        device_map='auto',
        use_auth_token=hf_auth
    )
    model.eval()

    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_id,
        use_auth_token=hf_auth
    )

    generate_text = transformers.pipeline(
        model=model,
        tokenizer=tokenizer,
        return_full_text=False,  # langchain expects the full text
        task='text-generation',
        temperature=0.1,  # 'randomness' of outputs, 0.0 is the min and 1.0 the max
        max_new_tokens=40,  # max number of tokens to generate in the output
        repetition_penalty=1.1  # without this output begins repeating
    )

    llm = HuggingFacePipeline(pipeline=generate_text)

    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    QnA = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        # chain_type_kwargs=chain_type_kwargs, # If you want to customize prompt, see example in custom_prompt.py
        return_source_documents=True
    )

    llm_response = QnA(query)
    print(llm_response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the main script with arguments.")
    parser.add_argument("--hf_auth", type=str, required=True, help="Hugging Face authentication token.")
    parser.add_argument("--persist_directory", type=str, required=True, help="Path to directory for vector database.")
    parser.add_argument("--query", type=str, required=True, help="Query for the language model.")

    args = parser.parse_args()
    main(args.hf_auth, args.persist_directory, args.query)
