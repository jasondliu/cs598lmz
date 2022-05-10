import mmap
import numpy as np
import sklearn

from scipy.io.wavfile import read
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#from sklearn.lda import LDA
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.externals import joblib

import sys

def load_test_data(test_file):
    test_data = np.loadtxt(test_file, delimiter=',', dtype='uint8')
    test_labels = test_data[:,0]
    test_images = test_data[:,1:]
    
    return test_labels, test_images

def load_train_data(train_file):
    train_data = np.loadtxt(train_file, delimiter=',', dtype='uint8')
