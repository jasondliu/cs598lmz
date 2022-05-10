import threading
threading.stack_size(50000000)

from os import mkdir
import sys, os
from collections import defaultdict
import numpy as np
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import RandomizedLasso
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest
from random import shuffle
import gc
from random import sample

if __name__ == '__main__':

    try:
        os.mkdir('./Results/')
