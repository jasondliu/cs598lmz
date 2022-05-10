import ctypes
# Test ctypes.CField_Proxy class
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int)]

class Y(X):
    _fields_ = [("b", c_int)]

class Z(Y):
    _fields_ = [("c", c_int)]

class A(Z):
    _fields_ = [("d", c_int)]

class Ptr(Pointer):
    _type_ = A

class Array(Y * 5):
    _length_ = 5

class Dict(Structure):
    _fields_ = [('array', Array), ('i', c_int)]

FAILED = 0

# ctypes.CField_Proxy calls the function __get__ on the field descriptor
# to implement instance attributes.
# The proxy doesn't have a __get__ method, so it inherits it from the type.
# We also call the __set__ method of the descriptor to implement assignment,
# and the __del__ method to implement deletion.
def test(obj, name, value):
    global FAILED

