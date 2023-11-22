import pickle
import streamlit as st
import numpy as np
import pandas as pd

st.header('Movie and Anime Recommender System')


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names




movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)



if st.button('Show Recommendation'):
   recommended_movie_names= recommend(selected_movie)
   for i in recommended_movie_names:
    st.write(i)



animes_dict = pickle.load(open('animes_dict.pkl','rb'))
similarity1 = pickle.load(open('similarity1.pkl', 'rb'))
animes = pd.DataFrame(animes_dict)
def recommend(anime):
   
    index = animes[animes["Name"] == anime]["index"].values[0]
    distances = sorted(list(enumerate(similarity1[index])), reverse=True, key=lambda x: x[1])
    recommended_anime_names = []
    for i in distances[1:6]:
        recommended_anime_names.append(animes.iloc[i[0]].Name)
    return recommended_anime_names


selected_anime = st.selectbox(
'Which anime did you like?',
(animes['Name'].values))

if st.button('Recommend'):
   recommended_anime_names = recommend(selected_anime)
   for i in recommended_anime_names:
    st.write(i)



