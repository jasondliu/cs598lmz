import ctypes
ctypes.cast(0, ctypes.py_object)
import theano
import theano.tensor as T
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.utils import shuffle
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split


def init_weights(shape):
    return theano.shared(np.random.randn(*shape) * 0.01)

def sigmoid(z):
    return 1/(1 + T.exp(-z))

def softmax(z):
    return T.nnet.softmax(z)

def relu(z):
    return T.maximum(z,0.)

def get_label(y,k):
    one_hot = np.zeros((y.shape[0], k ))
    for i in range(y.shape[0]):
        one_hot[i, y[i]] = 1
    return one_hot

def classification_rate(y_pred, y_true):
    return
