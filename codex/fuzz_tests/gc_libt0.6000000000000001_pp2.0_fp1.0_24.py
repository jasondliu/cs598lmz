import gc, weakref
import numpy as np

def _norm2(x):
    return np.linalg.norm(x.astype(np.float64))

class Caching:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Caching
def _f_ds(d, s):
    return 1 - s*np.sin(d)**2

@Caching
def _f_dd(d, d_):
    return np.cos(d)*np.cos(d_)

@Caching
def _f_ds_ds(d, s, s_):
    return s*np.sin(d)**2*s_*np.sin(d)**2

@Caching
def _f_ds_dd(d, s, d_):
    return -s*np.sin(d
