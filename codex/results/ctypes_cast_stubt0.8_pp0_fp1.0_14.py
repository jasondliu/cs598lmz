import ctypes
ctypes.cast(li[0], ctypes.py_object).value

# numpy
import numpy as np
arr = np.arange(10)
arr[5] = 42
arr

# Cython and NumPy
cimport cython
import numpy as np

cdef extern from "math.h":
    double sqrt(double m)

@cython.boundscheck(False)
@cython.wraparound(False)
def cy_sqrt(double[:] inp):
    cdef int i
    cdef double val
    cdef double[:] res = np.empty(inp.shape, dtype=np.float64)
    for i in range(inp.shape[0]):
        val = inp[i]
        res[i] = sqrt(val)
    return np.asarray(res)

def py_sqrt(inp):
    res = np.empty(inp.shape, dtype=np.float64)
    for i in range(inp.shape[0]):
        res
