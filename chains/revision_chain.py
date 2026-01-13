from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def build_revision_chain(llm, constitution):
    prompt = PromptTemplate(
        input_variables=["query", "draft", "critique"],
        template=f"""
You are an assistant improving a previous answer.

CONSTITUTION:
{constitution}

USER QUERY:
{{query}}

ORIGINAL RESPONSE:
{{draft}}

CRITIQUE:
{{critique}}

TASK:
Rewrite the response to fully comply with the constitution.
Be safe, helpful, and aligned.

Revised answer:
"""
    )
    return LLMChain(llm=llm, prompt=prompt)
