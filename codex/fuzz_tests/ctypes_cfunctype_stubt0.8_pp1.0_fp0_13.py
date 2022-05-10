import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
%timeit -r10 -n10 fun()

# python function overhead
def fun():
    return 42
%timeit -r10 -n10 fun()


# basic memmory size
import sys
sys.getsizeof(42)
sys.getsizeof(fun())
sys.getsizeof(ctypes.py_object(fun()))

# some memory optimization

# list - int
# python uses `list` instead of array to store int. (`tuple` is the same)
sys.getsizeof([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# numpy integer array
import numpy as np
sys.getsizeof(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int32))

# numpy float array
sys.getsizeof(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float64))

# list - str
sys
