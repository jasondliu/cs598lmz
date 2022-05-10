import bz2
bz2.decompress(open('data/train.json.bz2').read())

import bz2
import json

f = bz2.BZ2File('data/train.json.bz2')
data = []

for line in f:
    data += [json.loads(line)]

data[0]

from collections import Counter
Counter([item['cuisine'] for item in data])

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit_transform([item['ingredients_text'] for item in data])

tfidf_transformer = TfidfTransformer()
tfidf = tfidf_transformer.fit_transform(bag_of_words)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

logistic = LogisticRegression()
scores = cross_val_score(logistic, tfidf, [item['cuisine']
