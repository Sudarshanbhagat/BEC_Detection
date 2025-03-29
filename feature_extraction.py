import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Ensure NLTK resources are available
nltk.download("stopwords")

# Load preprocessed data
df = pd.read_csv("preprocessed_data.csv")

# Function to count stopwords
stop_words = set(stopwords.words("english"))
def count_stopwords(text):
    return sum(1 for word in text.split() if word in stop_words)

# Function to count special characters
def count_special_chars(text):
    return sum(1 for char in text if char in string.punctuation)

# Function to check for phishing keywords
phishing_keywords = ["invoice", "bank", "payment", "account", "urgent", "confirm", "security"]
def contains_phishing_words(text):
    return int(any(word in text.lower() for word in phishing_keywords))

# Extracting features
df["email_length"] = df["cleaned_message"].apply(lambda x: len(x.split()))
df["num_stopwords"] = df["cleaned_message"].apply(count_stopwords)
df["num_special_chars"] = df["cleaned_message"].apply(count_special_chars)
df["contains_phishing_words"] = df["cleaned_message"].apply(contains_phishing_words)

# TF-IDF Feature Extraction
vectorizer = TfidfVectorizer(max_features=100)
tfidf_features = vectorizer.fit_transform(df["cleaned_message"])

# Convert TF-IDF matrix to DataFrame
tfidf_df = pd.DataFrame(tfidf_features.toarray(), columns=vectorizer.get_feature_names_out())

# Combine extracted features with TF-IDF features
df = pd.concat([df, tfidf_df], axis=1)

# Save features to CSV
df.to_csv("features.csv", index=False)

print("Feature extraction complete! Saved as 'features.csv'.")
