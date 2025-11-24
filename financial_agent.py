from phi.agent import agent
from phi.model.groq import groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

#web search agent
web_search_agent=agent(
    name="Web search agent",
    role="Search the web for the information",
    model=groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include source"],
    show_tools_calls=True,
    markdown=True,
)

#financial agent

finance_agent=agent(
    name="Finance AI Agent",
    model=groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,
                      company_news=True),

    ],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent=agent(
    team=[web_search_agent,finance_agent],
    instructions=["Always include sources","use table to display the data"],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("summarize analyst recommendation and share the latest news for NVDA",stream=True)
