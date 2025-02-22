import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df = pd.read_csv(r"dataset\SA_SubTxt_fn.csv")
df = df.drop(['filename'], axis=1)

# Preprocessing the text
def preprocess_text(text):
    text = text.lower()
    text = text.replace('\n', ' ')  # Replace newline characters
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])  # Remove special characters
    return text

df['data'] = df['data'].apply(preprocess_text)

# Split the data into training and testing sets
X = df['data']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Convert text data into numerical features using TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Logistic Regression model
lr = LogisticRegression()
lr.fit(X_train_vec, y_train)

def PredictScamEmail(email):
    email_vec = vectorizer.transform([email])
    if lr.predict(email_vec)==0:
        return False
    else:
        return True




