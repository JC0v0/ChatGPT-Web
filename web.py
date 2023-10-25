from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from tools.tools import tools_name
from config import OPNEIA_API_BASE,OPNEIA_API_KEY,username,password
from memory.memory import memory,agent_kwargs,msgs
import chainlit as cl
from typing import Dict, Optional


@cl.password_auth_callback
def auth_callback(username: str, password: str) -> Optional[cl.AppUser]:
  if (username, password) == (username, password):
    return cl.AppUser(username=username, role="USER", provider="credentials")
  else:
    return None


@cl.set_chat_profiles
async def chat_profile():
    return [
        cl.ChatProfile(
            name="GPT-3.5",
            markdown_description="The underlying LLM model is **GPT-3.5-Turbo-16k**.",
            icon="https://chat.openai.com/favicon-32x32.png",
            
        ),
        cl.ChatProfile(
            name="GPT-4",
            markdown_description="The underlying LLM model is **GPT-4**.",
            icon="https://api.jingcheng.love/logo.png"
        ),
    ]

@cl.on_chat_start
def main():
    profile = cl.user_session.get("chat_profile")
    if profile == "GPT-3.5":
        model = "gpt-3.5-turbo-16k"
    else:
        model = "gpt-4"

    llm=ChatOpenAI(
        temperature=0.5,
        model=model,
        openai_api_base=OPNEIA_API_BASE,
        openai_api_key=OPNEIA_API_KEY,
        streaming=True
    )
    agent = initialize_agent(
        tools=tools_name,
        llm=llm,
        memory=memory,
        verbose=True,
        agent_kwargs=agent_kwargs,
        agent=AgentType.OPENAI_FUNCTIONS,
        
    )
    cl.user_session.set("agent", agent)

@cl.on_message
async def main(message: cl.Message):
   
    agent = cl.user_session.get("agent")

    res = agent.run(message.content,callbacks=[cl.LangchainCallbackHandler()])
    await cl.Message(content=res).send()