import weakref
import scipy
import scipy.optimize
import cv2

from lib.config import Config
import numpy as np @memoized(maxsize=None)
from functools import wraps
from time import time
import math
import os, sys

def profilefn(fn):
    '''Function Profiling Decorator'''
    
    @wraps(fn)
    def with_profiling(*args, **kwargs):
        start_time = time()

        ret = fn(*args, **kwargs)

        elapsed_time = time() - start_time

        if fn.__name__ not in PROF_DATA:
            PROF_DATA[fn.__name__] = [0, []]
        PROF_DATA[fn.__name__][0] += 1
        PROF_DATA[fn.__name__][1].append(elapsed_time)

        return ret

    return with_profiling

def print_prof_data():
    for fname, data in PROF_DATA.items():
        max_time = max(data
