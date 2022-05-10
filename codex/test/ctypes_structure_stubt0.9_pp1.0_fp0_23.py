import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p
    _fields_ = [('x', ctypes.c_void_p)]
