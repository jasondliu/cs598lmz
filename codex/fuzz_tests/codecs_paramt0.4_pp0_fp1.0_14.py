import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_data(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]   # header 제외
    return data

train_data = read_data('ratings_train.txt')
test_data = read_data('ratings_test.txt')

from konlpy.tag import Twitter
pos_tagger = Twitter()

def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
test_docs = [(tokenize(row[1]), row[2]) for row in test_data]

tokens = [t for d in train_docs for t in d[0]]

import nltk

