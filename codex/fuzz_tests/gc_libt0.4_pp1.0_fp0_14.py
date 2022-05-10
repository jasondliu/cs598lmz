import gc, weakref
import numpy as np
import random
import time
import sys
import multiprocessing as mp

def get_random_state(seed):
    if seed is None:
        return np.random.RandomState()
    if seed is np.random:
        return seed
    if isinstance(seed, (int, np.integer)):
        return np.random.RandomState(seed)
    if isinstance(seed, np.random.RandomState):
        return seed
    raise ValueError('%r cannot be used to seed a numpy.random.RandomState'
                     ' instance' % seed)

def get_random_state_or_1(seed):
    if seed is None:
        return 1
    if seed is np.random:
        return seed
    if isinstance(seed, (int, np.integer)):
        return seed
    if isinstance(seed, np.random.RandomState):
        return seed
    raise ValueError('%r cannot be used to seed a numpy.random.RandomState'
                     ' instance' % seed)

def get_random
