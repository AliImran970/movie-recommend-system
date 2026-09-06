# 🎬 Movie Recommendation System

A machine learning-based **Movie Recommendation System** that recommends 5 similar movies based on the movie selected by the user. The system uses content-based filtering and provides movie posters using the **TMDB API**.

## 🚀 Features

* 🎥 Select a movie from the available movie collection
* 🤖 Get 5 similar movie recommendations
* 🖼️ Display movie posters automatically
* 🔎 Content-based movie recommendation
* ⚡ Interactive web interface built with Streamlit
* 🌐 TMDB API integration for movie information and posters
* 📱 Simple and user-friendly interface

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Streamlit**
* **Requests**
* **Pickle**
* **TMDB API**

## 🧠 How It Works

The system uses **content-based filtering** to recommend movies.

The basic workflow is:

```text
Movie Dataset
     ↓
Data Preprocessing
     ↓
Feature Extraction
     ↓
Similarity Calculation
     ↓
Similarity Matrix
     ↓
User Selects a Movie
     ↓
Find Similar Movies
     ↓
Display Top 5 Recommendations
```

When a user selects a movie, the system finds movies with similar features and returns the **top 5 recommendations**.

## 📂 Project Structure

```text
movie-recommend-system/
│
├── app.py                 # Streamlit application
├── movie_dict.pkl         # Processed movie data
├── similarity.pkl         # Movie similarity matrix
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AliImran970/movie-recommend-system.git
```

### 2. Navigate to the project directory

```bash
cd movie-recommend-system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔑 TMDB API

The application uses the **TMDB API** to retrieve movie posters.

For production deployment, the API key should be stored securely using environment variables or the deployment platform's secrets management instead of directly exposing it in the source code.

## 🎯 Example

The user selects a movie such as:

```text
The Dark Knight
```

The system analyzes its movie features and returns five similar movies along with their posters.

## 📊 Machine Learning Approach

This project uses **content-based recommendation**, where movies are recommended based on their similarity to the selected movie.

The recommendation process can be summarized as:

```python
selected_movie
       ↓
Find movie index
       ↓
Retrieve similarity scores
       ↓
Sort movies by similarity
       ↓
Select top 5
       ↓
Fetch posters
       ↓
Display recommendations
```

## 🌐 Deployment

The application can be deployed using platforms such as:

* Streamlit Community Cloud
* Render
* Heroku
* Other Python-compatible cloud platforms

## 🔮 Future Improvements

* Add movie genres and ratings filters
* Add user-based recommendations
* Include movie ratings and release dates
* Add search functionality
* Improve recommendation accuracy
* Optimize the large similarity matrix
* Add a database for movie information
* Add user authentication
* Deploy the application with scalable cloud infrastructure

## 👨‍💻 Author

**Ali Imran**
 AI/ML Enthusiast

### ⭐ If you like this project

Give the repository a ⭐ on GitHub and feel free to contribute!
