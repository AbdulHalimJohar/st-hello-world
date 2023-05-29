import streamlit as st
import numpy as np

# Dummy data
num_users = 10
num_exercises = 5

np.random.seed(42)
user_exercise_matrix = np.random.randint(0, 6, size=(num_users, num_exercises))
np.random.seed(42)
social_link_matrix = np.random.randint(0, 2, size=(num_users, num_users))
np.fill_diagonal(social_link_matrix, 0)

def get_buddy_recommendation(user_id, user_exercise_matrix, social_link_matrix, k=5):
    user_index = user_id - 1
    user_preferences = user_exercise_matrix[user_index]
    
    similarities = []
    for i in range(user_exercise_matrix.shape[0]):
        if i != user_index:
            other_preferences = user_exercise_matrix[i]
            similarity = np.dot(user_preferences, other_preferences) / (np.linalg.norm(user_preferences) * np.linalg.norm(other_preferences))
            similarities.append((i, similarity))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_similar_users = similarities[:k]
    socially_connected_users = [user for user, _ in top_similar_users if social_link_matrix[user_index, user] == 1]
    
    return socially_connected_users

def main():
    st.title('Exercise Buddy Recommendation System')
    
    user_id = st.number_input('Enter your user ID:', min_value=1, max_value=num_users, value=1)
    num_recommendations = st.number_input('Number of buddies to recommend:', min_value=1, max_value=num_users-1, value=5)
    
    if st.button('Recommend'):
        recommendations = get_buddy_recommendation(user_id, user_exercise_matrix, social_link_matrix, num_recommendations)
        
        if recommendations:
            st.write('Top Buddy Recommendations:')
            for buddy in recommendations:
                st.write(f'- User {buddy + 1}')
        else:
            st.write('No recommendations found for the given user.')
            
  if __name__ == '__main__':
    main()
