import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load labeled dataset
df = pd.read_csv("features_labeled.csv")

# Ensure required columns exist
if 'cleaned_message' not in df.columns or 'label' not in df.columns:
    raise ValueError("Dataset must contain 'cleaned_message' and 'label' columns.")

# Drop any rows with missing values
df = df.dropna(subset=['cleaned_message', 'label'])

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['cleaned_message'])

# Target labels
y = df['label']

# Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Training Complete! Accuracy: {accuracy:.2f}")
print("📊 Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model and vectorizer
joblib.dump(model, "email_classifier.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("💾 Model and vectorizer saved successfully!")



