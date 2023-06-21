from langchain.chains import LLMChain, SequentialChain
from langchain import PromptTemplate
from prompt_templates import reply_template

class Replier():
    '''
    The information updater to update thoughts, status, and relationship.
    It is a wrapper function that sequentially calls the specific updater.
    '''
    def __init__(self, llm, agent_name, sender) -> None:
        self.llm = llm
        self.agent_name = agent_name
        self.sender = sender

    async def reply(self, report, message) -> str:
        reply_prompt = PromptTemplate(
            input_variables=["agent_name", "sender", "message", "report"],
            template=reply_template,
        )
        reply_chain = LLMChain(llm=self.llm, prompt=reply_prompt)
        reply = await reply_chain.arun(agent_name=self.agent_name,
                                 sender=self.sender,
                                 message=message,
                                 report=report)
        return reply
