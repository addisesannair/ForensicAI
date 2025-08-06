import streamlit as st
import openai
import os

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set title
st.title("Forensic AI Chatbot")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a forensic AI assistant."}]

# Display previous messages
for msg in st.session_state.messages[1:]:  # Skip system message
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input (better than text_input)
user_prompt = st.chat_input("Ask a question...")

if user_prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Call OpenAI chat model
    try:
        response = openai.ChatCompletion.create(
            model="ft:gpt-4o-2024-08-06:personal:forensicai:C1Na7epu",
            messages=st.session_state.messages,
            max_tokens=512,
            temperature=0.7
        )
        reply = response.choices[0].message["content"].strip()

    except Exception as e:
        reply = "Sorry, something went wrong."
        st.error(f"Error: {e}")

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
