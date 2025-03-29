from flask import Flask, request, jsonify
import joblib

# Load the trained model and vectorizer
MODEL_PATH = "C:/Users/hp/BEC_Detection/email_classifier.pkl"
VECTORIZER_PATH = "C:/Users/hp/BEC_Detection/tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if "message" not in data:
        return jsonify({"error": "No message provided"}), 400
    
    message = data["message"]
    text_vectorized = vectorizer.transform([message])  
    prediction = model.predict(text_vectorized)[0]  

    result = "BEC Attack 🚨" if prediction == 1 else "Normal Email ✅"
    
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
