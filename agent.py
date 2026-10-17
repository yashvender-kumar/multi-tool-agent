# Importation

from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from tools.calculator import calculator
from tools.pdf_rag import pdf_search
from tools.web_search import web_search 

#       LLM
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

# Tools List
tools = [calculator, pdf_search,web_search]

# System Promts
system_prompts = """
You are a helpful assistant with two tools.
- Use the calculator tool for any math or calculation.
- Use the pdf_search tool for questions about space facts from the PDF.
If a question needs both, use the tools one after another,
and give the final answer only when you have all the information.
"""


# Agents
agent = create_agent(llm, tools, system_prompt = system_prompts)


if __name__ == "__main__":
    print("Multi-Tool Agent ready! Band karne ke liye 'exit' likho.\n")

    while True:
        query = input("User: ")

        if query.strip().lower() in ["exit", "quit", "bye"]:
            print("Good Bye Have A Nice Day!")
            break

        # khali Enter pe dobara puchho
        if not query.strip():
            continue

        # error aaye to program crash na ho
        try:
            res = agent.invoke({"messages": [{"role": "user", "content": query}]})
            print("Ai:", res["messages"][-1].content, "\n")
        except Exception as e:
            print("Error:", e, "\n")
    