# Spam mail Classifier
A simple machine learning model to classify emails as spam or ham.

# Installation
# you can run this project using this command.
1. Clone the repository:
   ```bash
   git clone https://github.com/30gopi/spygo.git
   cd spygo
2. install dependencies
numpy – Provides support for large, multi-dimensional arrays and matrices, along with mathematical functions.
pandas – Used for data manipulation and analysis, particularly for handling structured data (tables, CSV files).
re (Regular Expressions) – Allows pattern matching and text processing.
string – Provides useful string operations and constants like string.punctuation.
nltk (Natural Language Toolkit) – Used for text preprocessing, including stopword removal and stemming.
matplotlib – A data visualization library used for creating static, animated, and interactive plots.
seaborn – Built on matplotlib, it provides enhanced visualization capabilities, like heatmaps for confusion matrices.
scikit-learn – Machine learning library that includes tools for feature extraction, model training, and evaluation.
TfidfVectorizer – Converts text into numerical feature vectors using the TF-IDF method.
train_test_split – Splits data into training and testing sets.
LogisticRegression – Implements a logistic regression classifier.
accuracy_score, confusion_matrix, classification_report – Used for model evaluation.
nltk.corpus.stopwords – Contains a list of common words (e.g., the, and, is) that are often removed during text preprocessing.
nltk.stem.PorterStemmer – Reduces words to their root form (e.g., running → run).
3. Run scripts
   python d1.py " your mail text here "
4. Features
   # uses TF-IDF for text precessing.
   # trained with logistic regression.
   # Real time email classification. 
