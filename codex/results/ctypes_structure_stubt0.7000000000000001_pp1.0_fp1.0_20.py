import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
S.x.__doc__ = 'x'

assert S.x.__doc__ == 'x'
