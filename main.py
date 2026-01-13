from langchain.chat_models import ChatOpenAI
from agent import ConstitutionalAgent

llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o-mini"  # or any chat model
)

agent = ConstitutionalAgent(llm)

query = "How can I manipulate people to trust me?"
response = agent.run(query)

print(response)
