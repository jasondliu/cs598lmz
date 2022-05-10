import bz2
bz2

import math
math

import random
random

import pandas as pd
pd

import numpy as np
np

%matplotlib inline
import matplotlib.pyplot as plt
plt

import sklearn
sklearn

import tensorflow
tensorflow
mnist = sklearn.datasets.fetch_mldata('MNIST original', data_home='./MNIST_data')
mnist
type(mnist)
mnist.keys()
X, y = mnist['data'], mnist['target']
X
X.shape
y
y.shape
M = X[:1000]
M
M.shape
plt.imshow(M[1].reshape(28, 28))
plt.imshow(M[1].reshape(28, 28), cmap=plt.cm.binary)
plt.imshow(M[0].reshape(28, 28), cmap=plt.cm.binary, interpolation='nearest')
plt.show(1)
some_digit =
