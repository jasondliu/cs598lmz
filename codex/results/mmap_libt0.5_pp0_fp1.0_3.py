import mmap
import re
import os
import sys
import time
import numpy as np

import theano
import theano.tensor as T
import lasagne

from lasagne.layers import InputLayer, DenseLayer, NonlinearityLayer, DropoutLayer
from lasagne.layers import MaxPool2DLayer as PoolLayer
from lasagne.layers import LocalResponseNormalization2DLayer as NormLayer
from lasagne.nonlinearities import softmax

import cPickle as pickle

class VGG_16:
    def __init__(self, input_var=None):
        self.net = {}
        self.net['input'] = InputLayer((None, 3, 224, 224), input_var=input_var)
        self.net['conv1_1'] = ConvLayer(self.net['input'], 64, 3, pad=1)
        self.net['conv1_2'] = ConvLayer(self.net['conv1_1'], 64, 3, pad=1)
        self.net['pool1'] = PoolLayer(self.net['conv1_
