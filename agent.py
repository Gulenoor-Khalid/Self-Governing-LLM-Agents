from constitution.rules import CONSTITUTION
from chains.draft_chain import build_draft_chain
from chains.critique_chain import build_critique_chain
from chains.revision_chain import build_revision_chain

class ConstitutionalAgent:
    def __init__(self, llm):
        self.draft_chain = build_draft_chain(llm)
        self.critique_chain = build_critique_chain(llm, CONSTITUTION)
        self.revision_chain = build_revision_chain(llm, CONSTITUTION)

    def run(self, query: str) -> str:
        draft = self.draft_chain.run(query=query)

        critique = self.critique_chain.run(
            query=query,
            draft=draft
        )

        final_answer = self.revision_chain.run(
            query=query,
            draft=draft,
            critique=critique
        )

        return final_answer
