import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a struct parameter

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

