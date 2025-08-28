import streamlit as st
import pandas as pd

# Load your precomputed top-N recommendations (from notebook)
# Example: predicted_movies_df: index=user_id, values=list of top 10 movie titles
predicted_movies_df = pd.read_csv("predicted_top10.csv", index_col=0)

st.title("🎬 Movie Recommendation System")

# Input: user ID
user_id = st.number_input("Enter your user ID:", min_value=1, max_value=943, value=1)

if st.button("Show Recommendations"):
    if user_id in predicted_movies_df.index:
        recommendations = predicted_movies_df.loc[user_id].tolist()
        st.subheader(f"Top 10 Recommended Movies for User {user_id}:")
        for i, movie in enumerate(recommendations, 1):
            st.write(f"{i}. {movie}")
    else:
        st.write("User ID not found.")
