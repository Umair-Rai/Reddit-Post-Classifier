Reddit Post Classifier
This project is an AI-powered web app that predicts the main category of a Reddit post (e.g., Gaming, Music, Education) using TF-IDF and Multinomial Naive Bayes. Built using Python, Scikit-learn, Flask, and deployed locally or with Ngrok for easy testing.

🔍 Enter a Reddit post title and get an instant category prediction!

📂 Features
✅ Text preprocessing using NLTK (lemmatization, stopword removal)

✅ Trained model with TF-IDF + Naive Bayes

✅ Label encoding/decoding

✅ Clean and simple Flask frontend (with index.html and result.html)

✅ Ngrok integration for one-click public sharing

🛠️ Tech Stack
Python 3.x

Scikit-learn

Flask

NLTK

Joblib

HTML/CSS

Ngrok

💡 Project Structure
cpp
Copy
Edit
📁 Reddit-Post-Classifier
├── reddit_category_model.pkl
├── tfidf_vectorizer.pkl
├── label_encoder.pkl
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/ (optional)
└── README.md
📦 Installation
Clone this repo:

bash
Copy
Edit
git clone https://github.com/Umair-Rai/Reddit-Post-Classifier.git
cd Reddit-Post-Classifier
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
<sup>(Include a requirements.txt with Flask, nltk, scikit-learn, joblib, pyngrok)</sup>

Download NLTK data:

bash
Copy
Edit
python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"
Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser:

Localhost: http://127.0.0.1:5000

Ngrok URL (will be printed in terminal)

📊 Example Prediction
Input:

arduino
Copy
Edit
"Should I upgrade my GPU for better gaming performance?"
Output:

yaml
Copy
Edit
Predicted Category: Gaming
🧠 Model Info
Vectorizer: TF-IDF

Classifier: Multinomial Naive Bayes

Dataset: Reddit post titles with labeled categories

📝 To-Do
 Add more categories

 Improve preprocessing with advanced NLP techniques

 Add support for post bodies

 Deploy to cloud (e.g., Render, Heroku)

🧑‍💻 Author
Made by Umair Akram 🔥
