import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulong(1)
    _fields_ = [('x', ctypes.c_ulong)]

