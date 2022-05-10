import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(*args):
    for i, arg in enumerate(args):
        print(i, arg)

f = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(func)
f(1, 2)
# Test ctypes.c_int.from_param()

import ctypes

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

c = C()
c.a = 1

ctypes.c_int.from_param(c)
# Test ctypes.c_int.from_param()

import ctypes

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

c = C()
c.a = 1

ctypes.c_int.from_param(c.a)
# Test ctypes.c_int.from_param()

import ctypes

class C(ctypes.Structure):
    _fields_
