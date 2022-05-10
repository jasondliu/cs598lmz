import ctypes
# Test ctypes.CFUNCTYPE on functions with struct arguments.
from ctypes import *
import _ctypes_test

class X(Structure):
    _fields_ = [("a", c_int), ("b", c_int)]

class Y(Structure):
    _fields_ = [("x", X), ("y", c_int)]

class Z(Structure):
    _fields_ = [("p", POINTER(Y)), ("z", c_int)]

def func(*args):
    print(list(args))

CFUNCTYPE(None, c_int, c_int)(func)(1, 2)
CFUNCTYPE(None, POINTER(c_int))(func)(pointer(c_int(42)))
CFUNCTYPE(None, POINTER(X))(func)(pointer(X(1, 2)))
CFUNCTYPE(None, POINTER(Y))(func)(pointer(Y(X(1, 2), 3)))
CFUNCTYPE(None, POINTER(Z))(func)(pointer(Z(pointer(Y(X(1, 2
