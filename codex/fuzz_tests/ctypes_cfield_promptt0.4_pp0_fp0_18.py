import ctypes
# Test ctypes.CField.from_address
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class Y(Structure):
    _fields_ = [("x", X),
                ("y", c_int)]

y = Y()

print(y.x.a)
print(y.x.b)
print(y.y)

print(y.x.__dict__)
print(y.__dict__)

print(y.x._objects)
y.x._objects[0] = 42
print(y.x.a)

print(y.x.b)
y.x.b = 43
print(y.x._objects)
print(y.x._b_base_)
print(y.x.b)

print(y.y)
y.y = 44
print(y.y)

print(y.x.__dict__)
print(y.__dict__)
