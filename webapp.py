from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from tools.tools import tools_name
from config import OPNEIA_API_BASE,OPNEIA_API_KEY
from memory.memory import memory,agent_kwargs,msgs
import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler

st.set_page_config(page_title="🦜🔗 JC-WebChat")
st.title(""" AI助手 JC-WebChat！ 🚀🤖
  
本项目集成了多种工具，可以使 ChatGPT 联网获取知识。

- 联网搜索
- 访问链接
- 维基百科知识库
- 新闻早报
- 网易云音乐热评
- 天气预报
- 快递查询
- 星座运势

无需使用任何指令，直接告诉 GPT 您的任务即可（仅ChatGpt可以使用工具）。

支持多种大语言模型。您可以在左侧的模型列表中查看具体信息。
""")


model = st.sidebar.selectbox(
    "请选择你的模型",
    ("gpt-3.5-turbo", "gpt-3.5-turbo-16k","gpt-3.5-turbo-0613","gpt-3.5-turbo-16k-0613" ,"gpt-4","gpt-4-0613","ERNIE-Bot","SparkDesk","qwen-v1","qwen-plus-v1")
)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7,step=0.1)
streaming = st.sidebar.checkbox("开启流式输出", value=True)
openai_api_base = st.sidebar.text_input("请输入你的OpenAI API Base",value=OPNEIA_API_BASE)
openai_api_key = st.sidebar.text_input("请输入你的OpenAI API Key",value=OPNEIA_API_KEY,type="password")
if not openai_api_key:
    st.info("输入 OpenAI API 密钥以继续, 如你没有OPENAI API KEY, 可请前往 [JC API](https://api.jingcheng.love) 获取API KEY ")
    st.stop()


llm=ChatOpenAI(
        temperature=temperature,
        model=model,
        openai_api_base=OPNEIA_API_BASE, 
        openai_api_key=openai_api_key,
        streaming=streaming
)
agent = initialize_agent(
    tools=tools_name,
    llm=llm,
    memory=memory,
    verbose=True,
    agent_kwargs=agent_kwargs,
    agent=AgentType.OPENAI_FUNCTIONS,
    
)
with st.sidebar:

    with st.expander("聊天记录"):
        for msg in msgs.messages:
            st.chat_message(msg.type).write(msg.content)

    if st.button("清除记忆"):
        msgs.clear()
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.markdown(
        """
         <a href="https://github.com/JC0v0/JC-WebChat" target="_blank" rel="JC-WebChat">
            <img src="https://badgen.net/badge/icon/GitHub?icon=github&amp;label=JC WebChat" alt="GitHub">
        </a>
 
        """
        , unsafe_allow_html=True)

if prompt := st.chat_input():
    st.chat_message("user",avatar="🧑").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(prompt, callbacks=[st_callback])
        st.markdown(response)
