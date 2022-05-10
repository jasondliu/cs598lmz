import mmap

from pymongo import MongoClient

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

from nltk import sent_tokenize, word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer
import nltk
from nltk.stem.porter import PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import normalize
from sklearn.metrics import precision_recall_curve, auc

import numpy as np
import pandas as pd
import os
from bs4 import BeautifulSoup
import re
import codecs
from sklearn import feature_extraction
import random
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

import sys
import os.path
import matplotlib.pyplot as plt
