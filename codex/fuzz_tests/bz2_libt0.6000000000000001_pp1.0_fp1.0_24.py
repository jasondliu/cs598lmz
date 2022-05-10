import bz2
bz2.BZ2File("train.ft.txt.bz2").readlines()
#bz2.BZ2File("train.ft.txt.bz2").readlines()[:10]

import os
os.getcwd()
os.listdir()

import pandas as pd

df = pd.read_csv("train.ft.txt", sep='\t', header=None)

df.head()

df.isnull().sum()

#from nltk.corpus import stopwords
#from string import punctuation
#stop_words = set(stopwords.words('english') + list(punctuation))

import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
stop_words = set(stopwords.words('english') + list(punctuation))

#def clean_review(review):
#    words = word_tokenize(review.lower())
#    words = [w for w in words if w not in stop_words]
