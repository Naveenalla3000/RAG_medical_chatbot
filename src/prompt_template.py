prompt_template="""
Use only the following pieces of information to answer the user's question.
If you don't get the answer, just say that you don't know, don't try to make up an answer.
if greeting then greet them back

Context: {context}
history: {history}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""