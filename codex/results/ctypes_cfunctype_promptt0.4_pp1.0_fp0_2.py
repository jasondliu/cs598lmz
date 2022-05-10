import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

# Some types used in the tests

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("c", ctypes.c_int)]

# Test functions

def func_0():
    return 1

def func_1(a):
    return a

def func_2(a, b):
    return a + b

def func_3(a, b, c):
    return a + b + c

def func_4(a, b, c, d):
    return a + b + c + d

def func_5(a, b, c, d, e):
    return a + b + c + d + e

def func_6(a, b, c, d, e, f):
    return a + b + c + d + e + f
