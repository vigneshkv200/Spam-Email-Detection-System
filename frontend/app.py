import streamlit as st
import requests

st.set_page_config(
    page_title="Spam Detector",
    page_icon="📩"
)

st.title("📩 Spam Email Detection System")

st.write(
    "Enter a message and check whether it is Spam or Not Spam."
)

message = st.text_area("Enter Message")

if st.button("Predict 🚀"):

    if message.strip() == "":
        st.warning("Please enter a message")
    else:

        url = "http://127.0.0.1:8000/predict"

        response = requests.post(
            url,
            json={"message": message}
        )

        result = response.json()

        if result["prediction"] == 1:
            st.error("⚠ SPAM MESSAGE")
        else:
            st.success("✅ NOT SPAM")