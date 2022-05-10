import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(12)
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

