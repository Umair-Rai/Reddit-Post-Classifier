🧠 Reddit Post Classifier
This project classifies Reddit posts into broad categories like Gaming, Education, Music, etc. using TF-IDF and a Naive Bayes classifier.

📂 Repository Structure
css
Copy
Edit
Umair-Rai/Reddit-Post-Classifier
│
├── NLP_Task_Project.ipynb          ← Main Jupyter Notebook
├── label_encoder.pkl               ← Saved Label Encoder
├── reddit_category_model.pkl       ← Trained Naive Bayes Model
├── tfidf_vectorizer.pkl            ← TF-IDF Vectorizer
├── README.md                       ← You are here
🚀 Run on Google Colab
Click below to open the notebook in Google Colab:


✅ Steps to Run Locally
Clone the repository:

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
Run the notebook:
Open NLP_Task_Project.ipynb in Jupyter or Colab and run all cells.

📦 Requirements
If not using Colab, install these:

bash
Copy
Edit
pip install scikit-learn pandas numpy
🧪 Model Details
Model: Multinomial Naive Bayes

Text Vectorization: TF-IDF

Categories: Broad Reddit categories (e.g., Gaming, Education, Music, etc.)

📌 Author
Umair Akram

