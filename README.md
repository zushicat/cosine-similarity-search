# cosine-similarity-search
Search short texts by cosine similarity of n-gram chars.

This is a very simple example of finding cocktail names. The base corpus is a list of cocktail names, found in
- /data/cocktailnames.txt

### Usage of scripts in /src
- 0_make_name_bi_grams.py
    - load corpus and transform each cocktail name into a string of bigrams, i.e.: "Zombie" -> "zo om mb bi ie"
- 1_save_train_vectors.py
    - load bigrams (saved in 0)
    - fit bigrams into a vectorizer and transform into a matrix

0 and 1 could be merged into one script, but creating n-grams of chars on a bigger corpus can be time consuming, thus it might be better to seperate these scripts.

- 2_load_predict_test.py
    - load vectorizer and matrix
    - load cocktailnames
    - create testset corpus and transform to bigrams
    - use loaded train_vectorizer on new corpus
    - calculate similarity
    - iterate over best results

The 5 best results for 4 requests (3 deliberatly misspelled):
```
magerita
    Margarita 0.47
    Mai Tai 0.42
    Strawberry Margarita 0.42
    Whitecap Margarita 0.42
    Blue Margarita 0.4

tonik vodka
    Vodka And Tonic 0.71
    Long vodka 0.62
    Vodka Martini 0.53
    Vodka Russian 0.42
    Kamikaze 0.35

caiprinja
    Caipirinha 0.62
    Dark Caipirinha 0.52
    Caipirissima 0.45
    Irish Spring 0.43
    Casino 0.33

mai tai
    Mai Tai 0.99
    Hawaiian Cocktail 0.45
    Shanghai Cocktail 0.43
    Martinez Cocktail 0.39
    Masala Chai 0.37
```

Here, the vectorization and similarity calculation is done the "scikit way".

But you certainly can take a look at /src/simple_example.py to see how to create a vector and the cosine similarity calculation "by hand". 

see also: https://stackoverflow.com/questions/1746501/can-someone-give-an-example-of-cosine-similarity-in-a-very-simple-graphical-wa
