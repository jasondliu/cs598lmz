import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def func(x):
    return np.exp(-x)

f = FUNTYPE(func)
f(1)

#%%
import ctypes
from ctypes import c_double

def func(x):
    return np.exp(-x)

f = ctypes.CDLL('./lib_test.so').func
f.argtypes = [c_double]
f.restype = c_double
f(1)

#%%
import ctypes
from ctypes import c_double

def func(x):
    return np.exp(-x)

f = ctypes.CDLL('./lib_test.so').func
f.argtypes = [c_double]
f.restype = c_double
f(1)

#%%

import ctypes
from ctypes import c_double

def func(x):
    return np.exp(-x)

f = ctypes.CDLL('./lib_test.so').func
f.argtypes = [
