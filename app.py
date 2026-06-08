import streamlit as st
import pickle
import pandas as pd

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #141e30, #243b55);
        color: white;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #FFD700;
        padding: 10px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
    }

    .stSelectbox label {
        color: white !important;
        font-size: 18px;
        font-weight: bold;
    }

    .stButton > button {
        background: linear-gradient(90deg, #ff416c, #ff4b2b);
        color: white;
        border: none;
        border-radius: 12px;
        height: 50px;
        width: 220px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: scale(1.05);
    }

    .movie-card {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 16px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)


# ---------- Recommendation Function ----------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# ---------- Load Data ----------
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# ---------- UI ----------
st.markdown('<div class="title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)

st.write("")

selected_movie_name = st.selectbox(
    '🎥 Choose your movie',
    movies['title'].values
)

st.write("")

# ---------- Button ----------
if st.button('✨ Recommend Movies'):
    recommendations = recommend(selected_movie_name)

    st.markdown("## 🍿 Top Recommendations")

    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for idx, movie in enumerate(recommendations):
        with cols[idx]:
            st.markdown(f"""
                <div class="movie-card">
                    🎬 <br><br>
                    <b>{movie}</b>
                </div>
            """, unsafe_allow_html=True)
