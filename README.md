
# 🎬 Movie Recommendation System

A Streamlit-based web app that recommends movies using a similarity matrix and fetches detailed information (poster, description, budget, release year, director, actors, and awards) from the TMDb and OMDb APIs.

---

## 🚀 Features
- Select a movie from a dropdown list
- Get top 5 similar movies based on cosine similarity
- Display posters for the selected and recommended movies
- Show detailed facts:
  - Overview / description
  - Budget
  - Release year
  - Director
  - Top 5 actors
  - Awards (via OMDb API)

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** (UI framework)
- **Pickle** (for saving/loading data)
- **TMDb API** (movie details, posters, credits)
- **OMDb API** (awards and IMDb data)

---
## 🔑 API Keys
- TMDb API → for posters, overview, budget, release year, director, actors
- OMDb API → for awards and IMDb data


## ⚙️ Setup Instructions
1. Clone the repository:
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system

2. Install dependencies:
   pip install -r requirements.txt

3. Add your API keys:
   - TMDb API key in app.py
   - OMDb API key in app.py

4. Run the app:
   streamlit run app.py


## 🌐 Deployment
Deploy easily on [Streamlit Cloud](https://streamlit.io/cloud) by connecting your GitHub repository.

