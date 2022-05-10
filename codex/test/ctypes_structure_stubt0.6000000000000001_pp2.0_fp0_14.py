import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [('x', ctypes.c_int)]

class S2(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [('x', ctypes.c_int), ('z', S)]

class S3(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [('x', ctypes.c_int), ('z', S2)]

s = S()
