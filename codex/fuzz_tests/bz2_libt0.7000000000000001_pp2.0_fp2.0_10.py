import bz2
bz2.BZ2File.readline = bz2.BZ2File.readlines

import numpy as np
import nltk
import scipy.io
import sklearn.metrics
import sklearn.cross_validation

def load_data(f, test=False):
    if isinstance(f, basestring):
        f = open(f, 'rb')
    X = []
    y = []
    for line in f:
        if test:
            X.append(line[:-1].split(','))
        else:
            try:
                y.append(line.split(',',1)[0])
                X.append(line.split(',',1)[1][:-1].split(','))
            except:
                print 'line:', line
                continue
    return np.array(X), np.array(y)

X, y = load_data('train.csv')

print 'train:', X.shape, y.shape

X_test, y_test = load_data('test.csv', test=True)
