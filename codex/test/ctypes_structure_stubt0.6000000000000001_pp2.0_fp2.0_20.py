import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()

class T(ctypes.Structure):
    _fields_ = [("s", S)]

s = S()
t = T()

