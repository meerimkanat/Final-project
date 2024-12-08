import os
import openai
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the message history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help?"}]

def get_assistant_response(messages):
    """
    Sends a request to OpenAI and retrieves a response from the assistant.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
    )
    return response["choices"][0]["message"]["content"]

# App title
st.title("BioQuest")

# Display message history
for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.markdown(f"**Assistant**: {message['content']}")
    else:
        st.markdown(f"**You**: {message['content']}")

# User input field
user_input = st.text_input("Your message:", key="user_input")

# Handle user input
if st.button("Send"):
    if user_input:
        # Add the user's message to the history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get the assistant's response
        assistant_response = get_assistant_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

        # Refresh the interface
        st.rerun()  # Updates the interface to show new messages

    
