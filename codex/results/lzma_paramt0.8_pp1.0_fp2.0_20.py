from lzma import LZMADecompressor
LZMADecompressor.decompress(s)

s = gzip.decompress(s)
s = s.decode("utf-8")

data = json.loads(s)

data[0]['text']

for d in data:
    print('\n')
    print(d['text'])

import gensim
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import numpy as np
import nltk

def sent_tokenize(text):
    sentences = nltk.sent_tokenize(text)
    sentences = [i.split() for i in sentences]
    return sentences

# tokenize the text in sentences
sentences = [i['text'] for i in data]
sentences = [sent_tokenize(i) for i in sentences]

len(sentences)

# Create the model
model = Word2Vec(sentences, min_count=1, size=300)

# Find a similar word for "mafia"
# model.wv.most_similar("mafia
