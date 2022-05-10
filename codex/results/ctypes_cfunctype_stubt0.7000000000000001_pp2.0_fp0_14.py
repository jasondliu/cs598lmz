import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
@jit
def f():
    return fun()
assert f()==42

# the following case failed in 8.9
import numpy
@jit
def f(a,b):
    return a+b
f(numpy.ones((4,4)), 2)
