import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int)]

def callback(x, y):
    print(x, y)

# calling convention
