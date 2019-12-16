# https://stackoverflow.com/questions/1746501/can-someone-give-an-example-of-cosine-similarity-in-a-very-simple-graphical-wa
import itertools
import math
import re
from collections import Counter

def get_ngrams(text, n=3):
	if len(text) == n:
		return [text]
	text = re.sub('\W+','', text)
	ngrams = zip(*[text[i:].lower() for i in range(n)])
	return [''.join(ngram) for ngram in ngrams]

def build_vector(iterable1, iterable2):
    counter1 = Counter(iterable1)
    counter2 = Counter(iterable2)
    all_items = set(counter1.keys()).union(set(counter2.keys()))
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

def cosim(v1, v2):
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2) )
    magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
    return dot_product / (magnitude1 * magnitude2)


l1 = "liköre"
l2 = "likör"
bi_grams_l1 = " ".join(itertools.chain(*[get_ngrams(w, 2) for w in l1.split()]))
bi_grams_l2 = " ".join(itertools.chain(*[get_ngrams(w, 2) for w in l2.split()]))

v1, v2 = build_vector(bi_grams_l1, bi_grams_l2)
print(cosim(v1, v2))
