import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
class V(ctypes.Structure):
    _fields_ = [('a', S * 1),
                ('b', S * 2)]
class P(ctypes.Structure):
    _anonymous_ = [('F', V)]
