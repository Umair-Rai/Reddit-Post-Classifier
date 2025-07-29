from flask import Flask, request, render_template
import joblib
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from pyngrok import ngrok
nltk.download('wordnet')
nltk.download('omw-1.4')

model = joblib.load("reddit_category_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

app = Flask(__name__)

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    text = text.lower()
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in ENGLISH_STOP_WORDS]
    return " ".join(words)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    post_text = request.form["post"]
    cleaned = preprocess_text(post_text)
    vectorized = vectorizer.transform([cleaned])
    label = model.predict(vectorized)[0]
    prediction = label_encoder.inverse_transform([label])[0]
    return render_template("result.html", prediction=prediction)

# Start Flask app via ngrok
if __name__ == "__main__":
    ngrok.set_auth_token("2zauZRSPdqjhHLsWBlo46xaK5yU_6n2XbifFQf8xoqi9HVZVA")
    public_url = ngrok.connect(5000)
    print("Public URL:", public_url)
    app.run(port=5000)
