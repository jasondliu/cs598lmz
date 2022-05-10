import gc, weakref, os
import numpy as np


class Subset(object):
    '''
    An object in which we can collect a subset of data.  This is inteneded
    to be used for a set of mass drifts for which we may want to compute
    the mean and variance.
    '''

    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def mean(self):
        return np.mean(self.data)

    def var(self):
        return np.var(self.data)


