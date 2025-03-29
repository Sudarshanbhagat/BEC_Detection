# BEC_Detection

📧 BEC Detection API
A Flask-based Business Email Compromise (BEC) detection API that analyzes email content to determine if it is a phishing attempt or a legitimate email. It uses Machine Learning (ML) models to classify emails as either:
✅ Safe (Legitimate Email)
❌ Compromised (Potential Phishing or BEC attack)


🛠 How It Works
Receives an email message through a POST request

Processes the text using a trained Machine Learning model

Classifies the message as either "Safe" or "Compromised"

Returns a JSON response with the classification result

📂 Project Structure
csharp
Copy
Edit
BEC_Detection/
│── app.py              # Flask API main file
│── model.pkl           # Trained ML model for classification
│── requirements.txt    # Python dependencies
│── static/             # Static files (if needed)
│── templates/          # HTML templates (if needed)
│── README.md           # Project documentation
└── .gitignore          # Git ignored files
🔧 Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/BEC_Detection.git
cd BEC_Detection
2️⃣ Set Up Virtual Environment
bash
Copy
Edit
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
▶️ Running the API Locally
bash
Copy
Edit
python3 app.py
🔹 Default URL: http://127.0.0.1:5500 (Change port if needed)
