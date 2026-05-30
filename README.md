# 🎬 Bollywood Movie Recommender

A content-based movie recommendation system that suggests Bollywood films based on your selection — powered by cosine similarity on a rich TMDB dataset, with a clean Streamlit interface.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)
![TMDB](https://img.shields.io/badge/Data-TMDB%20API-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Live Demo

👉 [Click here to try the app](https://movierecommender-snvfxeuypdkchuevn7n8x9.streamlit.app/)


---

## ✨ Features

- 🔍 **Content-Based Filtering** — Recommends movies using cosine similarity on combined feature vectors (genres, cast, crew, keywords, overview)
- 🎥 **TMDB API Integration** — Fetches real-time movie posters and metadata via The Movie Database API
- ⚡ **Streamlit UI** — Clean, interactive frontend with instant recommendations
- 📦 **Git LFS Support** — Large pickle/model files managed via Git Large File Storage for smooth deployment

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.10+ |
| Frontend | Streamlit |
| ML / Similarity | Scikit-learn (cosine similarity), CountVectorizer |
| Data Processing | Pandas, NumPy |
| Movie Data | TMDB API |
| Deployment | Streamlit Cloud |
| Large Files | Git LFS |

---

## 📁 Project Structure

```
bollywood-movie-recommender/
├── app.py                  # Streamlit app entry point
├── model/
│   ├── movies.pkl          # Preprocessed movie dataframe
│   └── similarity.pkl      # Cosine similarity matrix (tracked via Git LFS)
├── notebooks/
│   └── recommender.ipynb   # Data preprocessing & model building
├── screenshots/            # App screenshots for README
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/bollywood-movie-recommender.git
cd bollywood-movie-recommender
```

### 2. Install Git LFS (required for model files)

```bash
git lfs install
git lfs pull
```

### 3. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Set up TMDB API Key

Create a `.env` file in the root directory:

```
TMDB_API_KEY=your_api_key_here
```

> Get your free API key at [themoviedb.org](https://www.themoviedb.org/settings/api)

### 6. Run the app

```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501`

---

## 🧠 How It Works

1. Movie metadata (genres, cast, director, keywords, overview) is extracted from the TMDB dataset
2. All features are combined into a single "tags" string per movie
3. A **CountVectorizer** converts tags into feature vectors
4. **Cosine similarity** is computed between all movie vectors
5. On user selection, the top 5 most similar movies are returned along with their posters (fetched live via TMDB API)

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
requests
python-dotenv
```

> Full list in `requirements.txt`

---

## 🙋‍♂️ Author

**Soham Kale**



