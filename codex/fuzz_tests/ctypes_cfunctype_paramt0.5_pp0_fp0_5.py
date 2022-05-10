import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def wrap_function(lib, name, restype, argtypes):
    func = lib.__getattr__(name)
    func.restype = restype
    func.argtypes = argtypes
    return func

mylib = ctypes.cdll.LoadLibrary('./mylib.so')
myfunc = wrap_function(mylib, 'myfunc', ctypes.c_double, [ctypes.c_double])

print(myfunc(2))

# Cython

%load_ext cython

%%cython

cdef extern from "mylib.h":
    double myfunc(double)

print(myfunc(2))

# Cython with ctypes

%%cython

from libc.stdlib cimport malloc, free
from cpython cimport array

cdef extern from "mylib.h":
    double myfunc(double)
    
def wrap_function(func, argtypes, restype=None):
    func.arg
