import numpy as np
import pandas as pd
import re
import string
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK stopwords
nltk.download('stopwords')

# Load the dataset
df = pd.read_csv("spam.csv", encoding='ISO-8859-1')

# Drop unnecessary columns
df = df.iloc[:, :2]  # Keep only first two columns
df.columns = ['Label', 'Message']  # Rename for clarity

# Convert labels to binary (0 = Spam, 1 = Ham)
df['Category'] = df['Label'].map({'spam': 0, 'ham': 1})

# Preprocessing function
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]  # Remove stopwords
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]  # Apply stemming
    return ' '.join(words)

# Apply preprocessing
df['Processed_Message'] = df['Message'].apply(preprocess_text)

# Split data into features and labels
X = df['Processed_Message']
y = df['Category']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature extraction with TF-IDF
vectorizer = TfidfVectorizer()
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train_features, y_train)

# Evaluate the model
y_train_pred = model.predict(X_train_features)
y_test_pred = model.predict(X_test_features)

print("Training Accuracy:", accuracy_score(y_train, y_train_pred))
print("Testing Accuracy:", accuracy_score(y_test, y_test_pred))

# Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_test_pred), annot=True, fmt="d", cmap="Blues", xticklabels=['Spam', 'Ham'], yticklabels=['Spam', 'Ham'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

print("Classification Report:\n", classification_report(y_test, y_test_pred))

# Function to predict spam or ham for a given email
def predict_email(email_text):
    processed_email = preprocess_text(email_text)
    email_features = vectorizer.transform([processed_email])
    prediction = model.predict(email_features)
    return "Ham Mail" if prediction[0] == 1 else "Spam Mail"

# Test the function with a sample email
test_email = "Congratulations! You've won a free iPhone! Click here to claim."
print("Prediction:", predict_email(test_email))
