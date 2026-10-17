import streamlit as st

# Page setup 
st.set_page_config(page_title="Multi-Tool Agent", page_icon="🤖")

# Agent loading function
@st.cache_resource(show_spinner=False)
def load_agent():
    from agent import agent
    return agent

# Agent spinner 
with st.spinner("Agent loading..."):
    agent = load_agent()

st.title("🤖 Multi-Tool AI Agent")
st.caption("Calculator · Space PDF · Web Search")

# Sidebar for clear chat
with st.sidebar:
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show Previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# New Query
query = st.chat_input("Ask Anything...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                res = agent.invoke({"messages": st.session_state.messages})
                answer = res["messages"][-1].content
            except Exception as e:
                answer = f"Error: {e}"
            
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

            # For Execution => py -3.14 -m streamlit run app.py