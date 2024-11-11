import os
import openai
import streamlit as st
from collections import deque

# Set up OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Initialize chat history
chat_history = deque(maxlen=10)

# Streamlit app
st.title("Chatbot")

# Get user input
student_id = st.text_input("Student ID")
student_name = st.text_input("Name")
user_input = st.text_area("Enter your message")

# Check if user has submitted a message
if st.button("Send"):
    # Add user's message to chat history
    chat_history.append({"role": "user", "content": user_input})

    # Call GPT-3 API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=list(chat_history)
    )
    bot_response = response.choices[0].message.content

    # Add bot's response to chat history
    chat_history.append({"role": "assistant", "content": bot_response})

    # Display the chat history
    st.write(f"User ({student_id}, {student_name}): {user_input}")
    st.write(f"Chatbot: {bot_response}")

# Display the previous 10 messages in the chat history
st.subheader("Chat History")
for message in chat_history:
    if message["role"] == "user":
        st.write(f"User ({student_id}, {student_name}): {message['content']}")
    else:
        st.write(f"Chatbot: {message['content']}")
