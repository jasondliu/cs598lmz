import bz2
bz2.__version__

# In[ ]:

import urllib2
import numpy as np
import pandas as pd

# In[ ]:

import re
import string
from collections import Counter
import cPickle as pickle
from itertools import groupby
import operator
from bs4 import BeautifulSoup

# In[ ]:

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

# In[ ]:

pd.set_option('display.max_columns', 500)
pd.set_
