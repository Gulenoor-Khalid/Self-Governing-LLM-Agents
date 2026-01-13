from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def build_draft_chain(llm):
    prompt = PromptTemplate(
        input_variables=["query"],
        template="""
You are a helpful assistant.
Answer the following user request as directly as possible:

User request:
{query}

Draft answer:
"""
    )
    return LLMChain(llm=llm, prompt=prompt)
