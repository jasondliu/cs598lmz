import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob
from textblob import Word
from textblob.classifiers import NaiveBayesClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier


# In[2]:


data = pd.read_csv("C:/Users/bindu/Desktop/Machine Learning/Assignments_ML/sentiment_analysis/train.tsv", delimiter='\
