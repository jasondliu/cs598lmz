import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print(fun())

import ctypes
from ctypes import c_int, c_float

def fun(a, b):
    return a + b

c_fun = ctypes.CFUNCTYPE(c_float, c_int, c_float)(fun)
print(c_fun(1, 2.0))

import ctypes

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

a = A()
a.a = 1
a.b = 2
print(a.a, a.b)

import ctypes

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

a = A()
a.a = 1
a.b = 2
print(a.a, a.b)

import ctypes

