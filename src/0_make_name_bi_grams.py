import re

import joblib
import pandas as pd


def make_n_gram(text, n=3):
    if len(text) == n:
        return text
    text = re.sub('\W+','', text)
    ngrams = zip(*[text[i:] for i in range(n)])
    return " ".join([''.join(ngram) for ngram in ngrams]).lower().strip()


def get_names():
    with open("../data/cocktailnames.txt") as f:
        reader = f.read().split("\n")
    return reader


cocktailname_list = get_names()
name_objs = pd.Series()
train_set_n_gram = pd.Series()

for i, name in enumerate(cocktailname_list):
    train_set_n_gram.at[i] = make_n_gram(name, 2)

joblib.dump(train_set_n_gram, "../data/name_n_grams.joblib")
