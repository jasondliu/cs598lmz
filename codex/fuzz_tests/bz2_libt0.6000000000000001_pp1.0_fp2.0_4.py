import bz2
bz2.__version__

# In[2]:

import re
import os
import pandas as pd
import numpy as np
import pickle

from datetime import datetime
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from sklearn.linear_model import LogisticRegressionCV, SGDClassifier
from sklearn.metrics import f1_score, roc_auc_score, make_scorer, log_loss
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC, SVC
from sklearn.utils import shuffle

from nltk.corpus import stopwords

from matplotlib import pyplot as plt
plt.style.use('ggplot')
%matplotlib inline

# In[3]:

train = pd.read_csv('
