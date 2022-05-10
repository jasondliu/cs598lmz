import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

import pandas as pd
import random

import pickle

from text_clustering import *


def main():
    '''
    Main function
    '''
    # Loading data
    data = pd.read_csv('data/data.csv', encoding='utf-8')

    # Getting the sentences
    sentences = data['sentence'].values
    sentences = [str(sent) for sent in sentences]


