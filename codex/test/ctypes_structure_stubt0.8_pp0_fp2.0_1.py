import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("y", ctypes.c_int)]
    z = 2
    _fields_ = [("t", ctypes.c_int)]
# Make sure the type is S, not int
