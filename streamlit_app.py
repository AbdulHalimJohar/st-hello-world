import streamlit as st

# User input section
st.title("Find Your Workout Buddy")
st.write("Enter your exercise preferences:")

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
sport = st.text_input("Type of Sport")

# Process user input and get recommendations
if st.button("Find Buddy"):
    preferences = {
        "gender": gender,
        "sport": sport
    }
    
    # recommendations = get_buddy_recommendations(user_id=0, preferences=preferences)  # Assuming user_id = 0

    st.sidebar.title("Buddy Recommendations")
    #if recommendations:
    #    for recommendation in recommendations:
    #        st.sidebar.write(recommendation[0], f"Similarity Score: {recommendation[1]:.2f}")
    #else:
    #    st.sidebar.write("No recommendations found.")
