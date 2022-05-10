import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    __slots__ = 'x'

def f():
    X.x = 7

def g():
    X.x = ctypes.c_int

f()
g()
