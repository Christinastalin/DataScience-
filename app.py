import streamlit as st
import pickle


def recommend(selected_movie):
    # Get the index of the selected movie
    movie_index = movies[movies['title'] == selected_movie].index[0]

    # Get similarity scores for that movie
    similar_scores = list(enumerate(similarity[movie_index]))

    # Sort the movies based on similarity scores (excluding the movie itself)
    similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)[1:6]

    # Get the movie titles of top 5 matches
    top_5_titles = [movies.iloc[i[0]].title for i in similar_scores]
    return top_5_titles

st.header('Movie Recommender System')

#Load Data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox('Select Movie', movie_list)

if st.button('Show Recommendation'):
    st.subheader('Movie Recommendations:')
    for movie in recommend(selected_movie):
        st.write(movie)
