import pandas as pd
import joblib
import re

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ***************************************************
# load generated stuff
# ***************************************************
# vectorizer
train_vectorizer = joblib.load("../data/name_n_gram_vector.joblib")

# matrix
train_matrix = joblib.load("../data/name_n_gram_matrix.joblib")


# ***************************************************
#
# ***************************************************
def make_n_gram(text, n=3):
    if len(text) == n:
        return text
    text = re.sub('\W+','', text)
    ngrams = zip(*[text[i:] for i in range(n)])
    return " ".join([''.join(ngram) for ngram in ngrams]).lower().strip()


# ***************************************************
#
# ***************************************************
with open("../data/cocktailnames.txt") as f:
    cocktailnames = f.read().split("\n")


test_set = [
    "magerita",
    "tonik vodka",
    "caiprinja",
    "mai tai"
]

test_n_grams = pd.Series()
for i, row in enumerate(test_set):
    test_n_grams.at[i] = make_n_gram(row, 2)

test_matrix = train_vectorizer.transform(test_n_grams)  # use loaded train_vectorizer on new corpus
X = pd.DataFrame(cosine_similarity(test_matrix, train_matrix))  # calc. similarity

for i, row in X.iterrows():
    search_term = test_set[i]
    print(search_term)
    n_highest = row.nlargest(n=5)
    for j, value in n_highest.items():
        result_term = cocktailnames[j]
        print(f"    {result_term} {int(value*100)/100}")
    print()
