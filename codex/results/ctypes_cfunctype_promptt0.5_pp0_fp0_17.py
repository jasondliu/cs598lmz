import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

print f(1, 2)
print f(3, 4)

# Test ctypes.py_object

import sys

py_object = ctypes.py_object

class A(object):
    pass

a = A()
a.b = A()
a.b.c = A()
a.b.c.d = A()

a_obj = py_object(a)
print a_obj.b.c.d

# Test ctypes.cast

cast = ctypes.cast

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

x = X()
x.a = 1

print x.a
print cast(ctypes.pointer(x), ctypes.POINTER(ctypes.c_int)).contents.value

# Test c
