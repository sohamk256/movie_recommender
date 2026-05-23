import streamlit as st
import pickle


def load_data():
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies, similarity = load_data()

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values,
    index=None,
    placeholder="Search for a movie...",
)

if st.button("Recommend"):
    if selected_movie_name is None:
        st.warning("Please select a movie first!")
    else:
        recommendations = recommend(selected_movie_name)
        st.subheader("Recommended Movies:")
        for i, movie in enumerate(recommendations):
            st.write(f"{i+1}. {movie}")