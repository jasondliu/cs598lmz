import _struct
import sys
import os.path
import math
import numpy as np
import os

# from scipy.cluster.vq import *
# from scipy.spatial.distance import cdist

# from sklearn.cluster import KMeans
# from sklearn import metrics
# import matplotlib.pyplot as plt


def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels-idx1-ubyte'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images-idx3-ubyte'
                               % kind)
    with open(labels_path, 'rb') as lbpath:
        magic, n = _struct.unpack('>II',
                                  lbpath.read(8))
        labels = _np.fromfile(lbpath,
                              dtype=_np.uint8)

