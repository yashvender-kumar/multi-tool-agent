#  🤖 Multi-Tool AI Agent

An AI agent that reads a question, decides on its own which tool to use (calculator, PDF search or web search), and answers using the tool's result. Built with LangChain, Groq and Streamlit.

![App Screenshot](screenshot.png)

## Features

- **Calculator:** solves math expressions accurately instead of letting the LLM guess.
- **Space PDF (RAG):** searches a space facts PDF and answers from its content.
- **Web Search:** fetches the latest information from the internet using DuckDuckGo.
- **Chat memory:** remembers earlier messages, so follow-up questions work.
- **Streamlit UI:** simple chat interface with a clear-chat button.

## How It Works

```
User question
      ↓
LLM decides which tool is needed
      ↓
Tool runs (calculator / PDF search / web search)
      ↓
Tool result goes back to the LLM
      ↓
LLM gives the final answer
```

This loop is called the **ReAct pattern** (Reason + Act). If a question needs two tools, the agent uses them one after another, for example: find a number in the PDF, then multiply it with the calculator.

## Example Questions

- `234 * 56 solution?` → uses the calculator
- `What is a black hole?` → searches the PDF
- `What is Latest AI news?` → searches the web
- Follow-up: `Multiply by number 2` → uses chat memory

## Tech Stack
 -> Python
 -> Langchain (Agent $ Tool)
 -> Groq  (LLM)
 -> FAISS (vector store)
 -> HuggingFace embeddings
 -> DuckDuckGo Search
 -> Streamlit

 ## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yashvender-kumar/multi-tool-agent.git
cd multi-tool-agent
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install required dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables:** create a `.env` file in the project root and add:

```
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
```

5. **Add your PDF:** place a PDF file at `data/sample.pdf`.

6. **Run the Streamlit application:**

```bash
python -m streamlit run app.py
```

## Usage

1. **Launch the Application:** Run `python -m streamlit run app.py` in your terminal. The app opens at `http://localhost:8501`. The first start takes about a minute because the PDF and the embedding model are loaded.
2. **Ask a Question:** Type your query in the chat input at the bottom.
3. **Let the Agent Choose:** The agent decides on its own whether to use the calculator, the PDF search or the web search.
4. **Try Follow-ups:** The chat remembers earlier messages, so you can ask things like "Multiply that by 2".
5. **Clear the Chat:** Use the **Clear chat** button in the sidebar to start a new conversation.

## Roadmap

- [ ] Show which tool was used for each answer
- [ ] Source tracking with PDF page numbers
- [ ] Streaming responses
- [ ] PDF upload from the sidebar
- [ ] Support for multiple PDFs
- [ ] More tools (weather, Wikipedia)
- [ ] Safer calculator without `eval`
- [ ] Model fallback (Groq to Gemini)
- [ ] Deploy on Streamlit Community Cloud