# Importation
from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# Search object
Search = DuckDuckGoSearchRun()

# Tools
@tool
def web_search(query: str) -> str:
    """
    Search the internet for latest news, current events and
    real-time information.
    Use this tool when the answer may have changed recently or
    is not available in the PDF.
    Do not use it for math calculations or for space facts that
    are in the PDF.
    """

    try:
        result = Search.invoke(query)
        return result
    except Exception as e:
        return f"error: {e}"


if __name__=="__main__":
    print(web_search.invoke({"query": "Latest Ai News"}))
    

    


