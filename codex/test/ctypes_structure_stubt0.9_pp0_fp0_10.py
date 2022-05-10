import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p
# Explicitly assign this field, otherwise the last field may be unaligned
    _fields_ = [('x',ctypes.c_void_p)]
