import ctypes
ctypes.cdll.LoadLibrary("/usr/local/lib/libgfortran.so")
ctypes.cdll.LoadLibrary("/usr/local/lib/libquadmath.so")

from numpy.ctypeslib import ndpointer
import numpy as np

_lib = ctypes.CDLL('./lib_sum.so')
_func_sum = _lib.func_sum
_func_sum.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                      ctypes.c_int]
_func_sum.restype = ctypes.c_double

def func_sum(arr):
    return _func_sum(arr, arr.size)

if __name__ == '__main__':
    print(func_sum(np.arange(10)))
