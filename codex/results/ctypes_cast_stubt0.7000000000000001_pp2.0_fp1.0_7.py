import ctypes
ctypes.cast(x, ctypes.py_object).value

#%%
import numpy as np
def sum_arrays(x, y):
    return x+y

x = np.ones(10, dtype=np.int64)*3
y = np.ones(10, dtype=np.int64)*2

sum_arrays(x, y)

#%%
from numba import vectorize

@vectorize(["int64(int64,int64)"], target='parallel')
def sum_arrays(x, y):
    return x+y

x = np.ones(10, dtype=np.int64)*3
y = np.ones(10, dtype=np.int64)*2

sum_arrays(x, y)

#%%
from numba import vectorize

@vectorize(["int64(int64,int64)"], target='cuda')
def sum_arrays(x, y):
    return x+y

x = np.ones(10, dtype=np.int64)*3
y =
