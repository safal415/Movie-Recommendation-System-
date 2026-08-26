import streamlit as st
import pickle
import requests
import numpy as np

# Load dataframe and similarity matrix
movies_df = pickle.load(open("movies.pkl", "rb"))

# Load compressed similarity matrix from .npz
data = np.load("similarity.npz")
similarity = data["arr_0"]   # similarity matrix stored under default key

# Extract titles for dropdown
movies_list = movies_df['title'].values.tolist()

# API keys
TMDB_API_KEY = "021a74266cdfb503626006d7c245fdc0"
OMDB_API_KEY = "your_omdb_api_key_here"  # get one free at http://www.omdbapi.com/apikey.aspx

# Fetch movie ID from TMDb
def fetch_movie_id(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    response = requests.get(url).json()
    if response['results']:
        return response['results'][0]['id']
    return None

# Fetch movie details (poster, overview, budget, release year, director, actors)
def get_movie_details(movie_title):
    movie_id = fetch_movie_id(movie_title)
    if not movie_id:
        return None

    # TMDb details
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    details = requests.get(details_url).json()

    # Credits (actors & director)
    credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=en-US"
    credits = requests.get(credits_url).json()

    director = next((c['name'] for c in credits['crew'] if c['job'] == 'Director'), "Unknown")
    actors = [actor['name'] for actor in credits['cast'][:5]]

    # Poster
    poster = "https://image.tmdb.org/t/p/w500" + details['poster_path'] if details.get('poster_path') else None

    # OMDb awards (using imdb_id)
    awards = "Not available"
    if details.get('imdb_id'):
        omdb_url = f"http://www.omdbapi.com/?i={details['imdb_id']}&apikey={OMDB_API_KEY}"
        omdb_data = requests.get(omdb_url).json()
        awards = omdb_data.get('Awards', "Not available")

    return {
        "title": details.get('title', movie_title),
        "overview": details.get('overview', "No description available"),
        "budget": details.get('budget', 0),
        "release_year": details.get('release_date', "Unknown")[:4],
        "director": director,
        "actors": actors,
        "poster": poster,
        "awards": awards
    }

# Recommendation function
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    for i in movie_list:
        title = movies_df.iloc[i[0]].title
        recommended_movies.append(title)
    return recommended_movies

# Streamlit UI
st.title('🎬 Movie Recommendation System')

option = st.selectbox("Choose a movie:", movies_list)

if st.button("Recommend"):
    st.subheader(f"Details for: {option}")
    selected_details = get_movie_details(option)
    if selected_details:
        st.image(selected_details['poster'])
        st.write(f"**Overview:** {selected_details['overview']}")
        st.write(f"**Budget:** ${selected_details['budget']:,}")
        st.write(f"**Release Year:** {selected_details['release_year']}")
        st.write(f"**Director:** {selected_details['director']}")
        st.write(f"**Actors:** {', '.join(selected_details['actors'])}")
        st.write(f"**Awards:** {selected_details['awards']}")

    st.subheader("Top 5 Similar Movies:")
    names = recommend(option)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        details = get_movie_details(names[idx])
        if details:
            col.text(details['title'])
            if details['poster']:
                col.image(details['poster'])
            col.caption(f"{details['release_year']} | Dir: {details['director']}")
            col.write(f"Awards: {details['awards']}")
