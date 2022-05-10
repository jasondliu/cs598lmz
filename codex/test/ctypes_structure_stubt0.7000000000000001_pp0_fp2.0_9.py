import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [('y', ctypes.c_int)]

class D(S):
    pass

