
from langchain.tools import Tool
from langchain.tools.ddg_search.tool import DuckDuckGoSearchResults
from langchain.utilities import TextRequestsWrapper
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from tools.tool.zaobao import zaobao
from tools.tool.comment import comment
from tools.tool.weather import get_weather 
from tools.tool.joke import get_joke
from tools.tool.qinghua import get_qinghua
from tools.tool.check_express import kd
from tools.tool.constellation import Horoscope
requests = TextRequestsWrapper()
ddg_search = DuckDuckGoSearchResults()
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

tools_name = [
    Tool.from_function(
        func=ddg_search.run,
        name="ddg_search",
        description="useful for when you need to answer questions about current events",
        handle_tool_error=True,
    ),

    Tool.from_function(
        func=requests.get,
        name="Requests",
        description="Use it when you need to visit a link",
        handle_tool_error=True,
    ),

    Tool.from_function(
        func=wikipedia.run,
        name="Wiki",
        description="Wikipedia knowledge base, you can search for some useful knowledge",
        handle_tool_error=True,
    ),
    zaobao,
    comment,
    get_weather,
    get_joke,
    get_qinghua,
    kd,
    Horoscope,
]
