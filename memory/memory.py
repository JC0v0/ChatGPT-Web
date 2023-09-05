from langchain.memory import ConversationBufferMemory
from config import memory
from langchain.prompts import MessagesPlaceholder
from langchain.memory.chat_message_histories import ChatMessageHistory

agent_kwargs = {
    "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
}
msgs = ChatMessageHistory(key="special_app_key")

if memory == 'ConversationBufferMemory':

    memory = ConversationBufferMemory(chat_memory=msgs,memory_key="memory", return_messages=True)


