import bz2
bz2.BZ2File

def load_dataset():
    # Download dataset from http://ai.stanford.edu/~amaas/data/sentiment/
    f = bz2.BZ2File('/Users/abhishek/Downloads/aclImdb_v1.tar.gz')
    train_X, train_y = read_imdb('train', f)
    test_X, test_y = read_imdb('test', f)
    return train_X, train_y, test_X, test_y
train_X, train_y, test_X, test_y = load_dataset()
train_X[0]

"""
- Create a function that can turn a list of words into a set of vectors.
- Create another function that can turn a set of vectors into a set of words.
- Create a function that can create random sentences from the vectors.

"""

import pickle
import os
import numpy as np
f = open(os.path.join('data/imdb/imdb-train-val-test.p
