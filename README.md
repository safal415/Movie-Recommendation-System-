
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

![image alt] (media/Screenshot 2026-08-25 211157.png)
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


## 📂 Project Files
Whole project  is stored externally due to size limitations.  
Please go through this link to access them:

👉 [Download Required Files](https://drive.google.com/drive/folders/1lTdGwpJrKMMCo1H067D6-Dl4Exdc5SC4?usp=sharing)

## 📸 Demo

Here’s how the app looks:

![Movie Recommendation App Screenshot](https://github.com/safal415/Movie-Recommendation-System-/blob/safal415-patch-1/media/Screenshot%202026-08-25%20211157.png)
![App Screenshot](https://github.com/safal415/Movie-Recommendation-System-/raw/safal415-patch-1/media/Screenshot%202026-08-25%20215618.png)
![Second Screenshot](https://github.com/safal415/Movie-Recommendation-System-/raw/safal415-patch-1/media/Screenshot%202026-08-25%20215651.png)

