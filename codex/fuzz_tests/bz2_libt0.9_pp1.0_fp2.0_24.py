import bz2
bz2.BZ2File(open("data/vectors.txt.bz2", 'rb'))

import gzip
gzip.GzipFile(open("data/vectors.txt.bz2", 'rb'))

with open("data/vectors.txt", 'rb', buffering=10**9) as in_file:
    for line in in_file:
        pass

import _pickle as cPickle

model = cPickle.load(open("data/model.pkl", 'rb'))

model = cPickle.load(open("data/model.pkl", 'r'))


with open("data/vectors.txt", 'r') as in_file:
    for line in in_file:
        pass

import _pickle as cPickle
model = cPickle.load(open("data/model.pkl", 'r'))

!pip install nltk==3.2.1

import nltk
nltk.download("stopwords")
#model = gensim.models.Keyed
