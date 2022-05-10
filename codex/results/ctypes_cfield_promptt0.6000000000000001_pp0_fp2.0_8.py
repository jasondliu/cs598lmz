import ctypes
# Test ctypes.CField
from ctypes import *

class X(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", c_int),
        ("c", c_int)]

x = X()
print x.a, x.b, x.c
x.a = 1
x.b = 2
x.c = 3
print x.a, x.b, x.c

# Test ctypes.CField.from_param
from ctypes import *

def get_buffer(buf):
    return buf

class X(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", c_int),
        ("c", c_int)]

x = X()
x.a = 1
x.b = 2
x.c = 3

# XXX: is this a bug?
#print get_buffer(x)

# Test ctypes.CField.from_address
from ctypes import *

class X(Structure):
    _fields_ = [
        ("a", c_
