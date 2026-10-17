# Importaion 

from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# Load Pdf
loader = PyPDFLoader("data/sample.pdf")
docs = loader.load()

# Spliting
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000, 
    chunk_overlap = 250
)

chunk = text_splitter.split_documents(docs)

# Embbeding
embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

# Vector Store and Reterval
vectorstore  = FAISS.from_documents(chunk,embedding)
retriever = vectorstore.as_retriever(search_kwargs = {"k": 3})

# Tool Fucntion
@tool
def pdf_search(question: str) -> str:
    """
    Search the space facts PDF and return the most relevant parts.
    Use this tool for questions about space, planets, stars, galaxies,
    black holes, the solar system, astronauts or space missions.
    Do not use it for math calculations or latest internet news.
    """
    try:
        result = retriever.invoke(question)
        return "\n\n".join(doc.page_content for doc in result)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Pages:", len(docs))
    print("Chunk:", len(docs))
    print(pdf_search.invoke({"question": "Tell me about?"})) 

    

