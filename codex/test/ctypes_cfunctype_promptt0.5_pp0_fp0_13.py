import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
import _ctypes_test

class X(Structure):
    _fields_ = [("a", c_int)]

class Y(Structure):
    _fields_ = [("b", c_int)]

# CFUNCTYPE(None)
c_func = CFUNCTYPE(None)(lambda: None)

# CFUNCTYPE(c_int)
c_func = CFUNCTYPE(c_int)(lambda: None)

# CFUNCTYPE(c_int, c_int)
c_func = CFUNCTYPE(c_int, c_int)(lambda x: None)

# CFUNCTYPE(c_int, c_int, c_int)
c_func = CFUNCTYPE(c_int, c_int, c_int)(lambda x, y: None)

# CFUNCTYPE(c_int, c_int, c_int, c_int)
