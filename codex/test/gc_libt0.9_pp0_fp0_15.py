import gc, weakref
import random, threading

try:
    import cPickle as pickle
except ImportError:
    import pickle

