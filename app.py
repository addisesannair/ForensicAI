import openai
import streamlit as st

# Step 1: Set up OpenAI API Key
openai.api_key = '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'

# Step 2: Fine-tuned model ID
fine_tuned_model_id = 'ft:gpt-4o-2024-08-06:personal:forensicai:C1Na7epu'  # Replace this with your fine-tuned model ID

# Step 3: Streamlit UI for chatbot
st.title("Forensic AI Chatbot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Step 4: Get user input
user_input = st.text_input("Ask a question:")

# Step 5: When user inputs a message, call the fine-tuned model
if user_input:
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate a response from the fine-tuned model
    try:
        response = openai.Completion.create(
            model=fine_tuned_model_id,
            prompt=user_input,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        assistant_response = response.choices[0].text.strip()

        # Add assistant's response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    except Exception as e:
        assistant_response = "Sorry, there was an error processing your request."
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        st.error(f"Error: {e}")

# Step 6: Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"*You*: {message['content']}")
    else:
        st.markdown(f"*AI*: {message['content']}")
