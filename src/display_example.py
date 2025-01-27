"""
This Streamlit application allows users to search for trainers by name.

It sends a GET request to a FastAPI endpoint to retrieve trainer data and filters the results
based on user input.

Dependencies:
- streamlit: For building the web interface.
- requests: For sending HTTP requests to the API.

How It Works:
1. Users enter a trainer's name into the text input field.
2. On clicking the 'Submit' button, the application fetches trainer data from the API.
3. The application displays the trainer details if the name matches the user input.
"""

import streamlit as st
import requests

# Text input for searching trainers
text = st.text_input("Search by trainer: ")

# Submit button to trigger the search
submit = st.button("Submit")

if submit:
    """
    Fetch and display trainer details based on user input.

    The function sends a GET request to the FastAPI endpoint to retrieve all trainers.
    It then filters the results to find the trainer whose name matches the input.
    """
    result = requests.get("http://127.0.0.1:3333/trainers").json()

    for trainer in result:
        if trainer["name"] == text:
            st.write(trainer)
