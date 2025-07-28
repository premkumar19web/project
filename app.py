import streamlit as st
from langchain.llms import Ollama
from langchain.chains import ConversationChain
from memory import get_memory

# Streamlit page setup
st.set_page_config(page_title="🧠 Local Chatbot with Memory", layout="centered")
st.title("🧠 Chatbot with Memory (Offline using Ollama)")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize LLM and memory
llm = Ollama(model="mistral")  # You can also use 'llama2', 'gemma', etc.
memory = get_memory()

# Create conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Input box
user_input = st.text_input("You:", "")

if user_input:
    # Get model response
    response = conversation.run(user_input)

    # Save interaction in session
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    st.chat_message("user" if speaker == "You" else "assistant").write(msg)
