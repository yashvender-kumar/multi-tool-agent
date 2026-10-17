# Importation

from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

# Tool function 

@tool
def calculator(expression: str) -> str:
    """
    Solve Mathmetical Calculation (
    like: Additon, Subtraction, Multiplication, Division and Power).
    When do calculation of any number or digit so, use this tool
    """


    # ---------- Step 3: Expression evaluate karo ----------
    try:
        #Disabled built-in functions so that no dangerous code can run.
        result = eval(expression, {"__builtins__": {}}, {})

        #  Result return 
        return str(result)

    #  Error handling 
    except Exception as e:
        
        return f"Error: {e}"


if __name__=="__main__":
    print(calculator.invoke({"expression": "234 * 56"}))
    print(calculator.invoke({"expression": "(100 + 50)/3"}))
    print(calculator.invoke({"expression": "abc +"}))

    