import ctypes
# Test ctypes.CField.from_param
from ctypes import *

class X(Structure):
    _fields_ = [
        ("x", c_int),
        ("y", c_int),
    ]

class Y(X):
    _fields_ = [
        ("z", c_int),
    ]

def f(x):
    return x.x + x.y

f.argtypes = c_int,
f.restype = c_int

assert f(X(1, 2)) == 3
assert f(Y(1, 2, 3)) == 3

# Test ctypes.CField.from_param
from ctypes import *

class X(Structure):
    _fields_ = [
        ("x", c_int),
        ("y", c_int),
    ]

class Y(X):
    _fields_ = [
        ("z", c_int),
    ]

def f(x):
    return x.x + x.y

f.argtypes = c_int,
f.restype = c_int


