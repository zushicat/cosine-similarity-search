import joblib
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

name_bi_grams = joblib.load("../data/name_n_grams.joblib")  # load bigrams

train_vectorizer = vectorizer.fit(name_bi_grams)  # vectorizer
train_matrix = train_vectorizer.transform(name_bi_grams) # matrix

joblib.dump(train_vectorizer, "../data/name_n_gram_vector.joblib")
joblib.dump(train_matrix, "../data/name_n_gram_matrix.joblib")
