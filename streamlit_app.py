import streamlit as st

# User input section
st.title("Find Your Workout Buddy")
st.write("Enter your exercise preferences:")

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
sport = st.text_input("Type of Sport")
