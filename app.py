import streamlit as st
from dotenv import load_dotenv
import os
import requests

load_dotenv()

Api = os.getenv("api")

# Title
st.title("Check Question Level")

# Input
question = st.text_input("Enter your Question")

# Button to send the request
if st.button("Click me"):
    if question:
        with st.spinner("Processing..."):
            # API request payload
            payload = {"prompt": question}

            # Send request
            try:
                response = requests.post(Api, json=payload)
                if response.status_code == 200:
                    answer = response.json().get("response", "No response received")
                    st.success(f"Response: {answer}")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter a question first.")
