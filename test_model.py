import joblib
import sys
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
model_path = r"C:\Users\hp\BEC_Detection\email_classifier.pkl"
vectorizer_path = r"C:\Users\hp\BEC_Detection\tfidf_vectorizer.pkl"

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    print("✅ Model and vectorizer loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model/vectorizer: {e}")
    sys.exit(1)

def classify_email(text):
    """Predict if an email is BEC (1) or normal (0)."""
    text_vectorized = vectorizer.transform([text])  # Convert text into numerical format
    prediction = model.predict(text_vectorized)[0]  # Get prediction
    return "🚨 BEC Attack" if prediction == 1 else "✅ Normal Email"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        email_text = sys.argv[1]  # Read email text from command line
        result = classify_email(email_text)
        print(f"\n📩 **Prediction:** {result}")
    else:
        print("\n❌ Please provide an email message as input.")
