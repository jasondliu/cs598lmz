import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short

class C(ctypes.Structure):
    _fields_ = [("s", S)]

s = S()
