import streamlit as st
import pickle
import pandas as pd
import requests

# ---------- Page settings (UI only) ----------
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")


def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id)
    response = requests.get(url)
    data = response.json()

    poster_path = data.get('poster_path')
    if poster_path:
        return 'https://image.tmdb.org/t/p/w500/' + poster_path
    else:
        return 'https://via.placeholder.com/500x750?text=No+Image'


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # actual TMDB id column — rename if yours differs
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------- Header (UI only) ----------
st.title("🎬 Movie Recommender System")
st.markdown("Pick a movie you like, and we'll suggest 5 similar ones for you to watch next.")
st.divider()

selected_movie_name = st.selectbox('🎥 Here is your favourite movies', movies['title'].values)

if st.button('✨ Recommend', use_container_width=True):
    with st.spinner('Finding movies you might like...'):
        names, posters = recommend(selected_movie_name)

    st.divider()
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0], use_container_width=True)
        st.caption(f"**{names[0]}**")
    with col2:
        st.image(posters[1], use_container_width=True)
        st.caption(f"**{names[1]}**")
    with col3:
        st.image(posters[2], use_container_width=True)
        st.caption(f"**{names[2]}**")
    with col4:
        st.image(posters[3], use_container_width=True)
        st.caption(f"**{names[3]}**")
    with col5:
        st.image(posters[4], use_container_width=True)
        st.caption(f"**{names[4]}**")