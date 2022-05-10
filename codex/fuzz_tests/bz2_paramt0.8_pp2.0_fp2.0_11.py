from bz2 import BZ2Decompressor
BZ2Decompressor.buf_size = 500 * 1024 * 1024

import pandas as pd
import gensim
word2vec = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

def get_vector(word):
    return word2vec.wv[word]

def get_vector_for_doc(doc):
    vectors_for_doc = []
    for word in doc:
        vectors_for_doc.append(get_vector(word))
    return vectors_for_doc

from nltk import ngrams, word_tokenize
def construct_ngram(doc,grams):
    grams_in_doc = []
    for n in grams:
        grams_in_doc.extend(list(ngrams(word_tokenize(doc),n)))
    return [gram for gram in grams_in_doc if len(gram) > 1 and len(gram) <= 7]

from sklearn.cluster import DBSCAN
import numpy as np
from sk
