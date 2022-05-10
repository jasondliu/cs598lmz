import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(a, b):
    print a, b

FUNC = CFUNCTYPE(None, c_int, c_int)(func)

FUNC(1, 2)

# Test ctypes.POINTER

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int)]

x = X()
x.a = 42

p = pointer(x)
print p.contents.a

# Test ctypes.byref

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int)]

x = X()
x.a = 42

p = byref(x)
print p.contents.a

# Test ctypes.addressof

from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int)]

x = X()
x.a = 42

p = addressof(x)
print p.contents.
