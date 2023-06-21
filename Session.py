from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

import asyncio
from getpass import getpass
import os

from InfoUpdater import InfoUpdater
from Replier import Replier
from InfoCollector import InfoCollector

OPENAI_API_KEY = ''

class Session():
    '''
    The Session class is the at the top level to handle a conversation with a user.
    It should be created when a session is established.
    When the session is end, it automatically summrize the short-term context into a long-term memory.
    '''
    def __init__(self, OPENAI_API_KEY, agent_name, sender) -> None:
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
        self.llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=1, model="gpt-3.5-turbo-0613")
        self.agent_name = agent_name
        self.sender = sender

        # Load thoughts file to ChromaDB
        thoughts_loader = TextLoader('./config/thoughts.txt')
        thoughts_documents = thoughts_loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 150,
            chunk_overlap  = 20,
            length_function = len,
        )
        docs = text_splitter.split_documents(thoughts_documents)
        embeddings = OpenAIEmbeddings()
        self.db = Chroma.from_documents(docs, embeddings, persist_directory="./chromadb/")
        print('Initialized ChormaDB...')
        # self.db.persist()

        # Create instances
        self.collector = InfoCollector(llm=self.llm, agent_name=self.agent_name,sender=self.sender,)
        self.replier = Replier(llm=self.llm, agent_name=self.agent_name,sender=self.sender)
        self.updater = InfoUpdater(llm=self.llm, agent_name=self.agent_name, sender=self.sender, db=self.db)

    async def reply(self, message) -> str:
        report = await self.collector.collect(message=message)
        reply_info = await self.replier.reply()
        # update_info = await self.collector.update()

#asyncio.run(iu.update_thoughts(agent_name="Sam", sender="Dean",conversation=conversation))
#asyncio.run(ic.collect(message="What do you think of me?",sender="Tom"))

# db = Chroma(persist_directory="./chromadb/", embedding_function=OpenAIEmbeddings())
# db.similarity_search("")

