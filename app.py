import openai
import streamlit as st
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fine-tuned model ID (must be a chat model like gpt-4o)
fine_tuned_model_id = 'ft:gpt-4o-2024-08-06:personal:forensicai:C1Na7epu'

# Streamlit UI
st.title("Forensic AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a forensic AI assistant."}]

# Get user input
user_input = st.text_input("Ask a question:")

# Handle user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model=fine_tuned_model_id,
            messages=st.session_state.messages,
            max_tokens=150,
            temperature=0.7
        )
        assistant_response = response.choices[0].message["content"].strip()
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    except Exception as e:
        assistant_response = "Sorry, there was an error processing your request."
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        st.error(f"Error: {e}")

# Display chat history
for message in st.session_state.messages[1:]:  # Skip system prompt
    if message["role"] == "user":
        st.markdown(f"**You**: {message['content']}")
    else:
        st.markdown(f"**AI**: {message['content']}")
