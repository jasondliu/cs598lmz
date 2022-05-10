import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int)]

class S2(S):
    _fields_ = [('y', ctypes.c_int)]

class S3(S2):
    _fields_ = [('z', ctypes.c_int)]

