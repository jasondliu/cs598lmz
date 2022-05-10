import ctypes
ctypes.cdll.LoadLibrary('/usr/lib/atlas-base/atlas/liblapack.so')
ctypes.cdll.LoadLibrary('/usr/lib/atlas-base/atlas/libf77blas.so')
ctypes.cdll.LoadLibrary('/usr/lib/atlas-base/atlas/libcblas.so')

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import tree
import pickle

from slow_test_warnings import conv_warn, runtime_warn

from time import time
from optparse import OptionParser

from general_functions import load_gt_csv, train_and_test, load_csv_results, \
        plot
