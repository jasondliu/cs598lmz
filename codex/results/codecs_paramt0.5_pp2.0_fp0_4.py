import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))
import re
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
import gensim
from gensim import corpora
import string
import numpy as np

# load data
def load_data(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    return text

# split a document into parsed sentences
def tokenize_sentences(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    return sentences

# remove stop words
def remove_stopwords(tokens):
    stoplist = stopwords.words('english')
    return [word for word in tokens if word not in stoplist]

# remove punctuations
def remove_punctuations(tokens):
    punct
