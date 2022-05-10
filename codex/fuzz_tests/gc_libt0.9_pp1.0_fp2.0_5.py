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


class Trial(object):
    '''
    An experimental trial, encapsulating an isobaric, weakly-coupled, force
    measurement (or tug), including next neighbor, flexible linker and all
    bead types.  The bead type may be explicitly stored, but a linkage object
    will be created which holds these data implicitly.  Experimental
    parameters are held as attributes, including buffer and ligand
    concentration.  More attributes will be added as needed.  A plot object
    and controller are
