import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

import warnings
warnings.filterwarnings('ignore')

%matplotlib inline
 
# Загружаем данные
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Объединяем датас
