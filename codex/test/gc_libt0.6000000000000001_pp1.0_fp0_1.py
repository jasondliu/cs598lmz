import gc, weakref
import os
import time
import sys

try:
    import cPickle as pickle
except ImportError:
    import pickle

