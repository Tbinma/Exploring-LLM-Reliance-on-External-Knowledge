from langchain.prompts import PromptTemplate

# the default prompt
print(QnA.combine_documents_chain.llm_chain.prompt.template)



# Define your prompt template
prompt_template = """
Consider the following context when answering the question. Don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:
"""

# Create the PromptTemplate
PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# Define the chain type kwargs with the custom prompt
chain_type_kwargs = {"prompt": PROMPT}


#add chain_type_kwargs=chain_type_kwargs in the main ()

# QnA = RetrievalQA.from_chain_type(llm=llm,
#                                   chain_type="stuff",
#                                   retriever=retriever,
#                                   chain_type_kwargs=chain_type_kwargs,
#                                   return_source_documents=True)