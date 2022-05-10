import ctypes

class S(ctypes.Structure):
    x = 8
    _fields_ = [('y', ctypes.c_long) ]
    _packed_ = True

size = ctypes.sizeof(S)
