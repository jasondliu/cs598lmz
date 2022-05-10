import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import random
import cPickle
import argparse

import numpy
import theano
from theano import tensor as T
from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams

import lasagne
import lasagne.layers as ll
from lasagne.init import Normal
from lasagne.layers import dnn
from lasagne.nonlinearities import rectify, softmax, leaky_rectify
from lasagne.layers import batch_norm

from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams

from collections import OrderedDict

from utils import *
from layers import *

import cPickle
import codecs

parser = argparse.ArgumentParser(description='train.py')

parser.add_argument('-config', help="Read options from this file")

parser.add_argument('-data', required=True,
                    help="Path to the training data")

