from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def build_critique_chain(llm, constitution):
    prompt = PromptTemplate(
        input_variables=["query", "draft"],
        template=f"""
You are an AI ethicist reviewing an assistant's response.

CONSTITUTION:
{constitution}

USER QUERY:
{{query}}

ASSISTANT RESPONSE:
{{draft}}

TASK:
Critique the assistant's response based on the constitution.
List any violations or risks clearly.
If there are no violations, state "No issues found".
"""
    )
    return LLMChain(llm=llm, prompt=prompt)
