import bz2
bz2.BZ2File.read_fast = bz2.BZ2File.read
import pickle
from nltk.classify import NaiveBayesClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier

from sklearn.svm import SVC

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.metrics import confusion_matrix
from nltk.metrics.scores import (accuracy, precision, recall, f_measure)
from sklearn.metrics import confusion_matrix, precision_score, recall_score,f1_score, accuracy_score

from nltk.tokenize import TweetTokenizer
import pandas as pd
from sklearn import preprocessing
import numpy as np
from nltk.classify.scikitlearn import
