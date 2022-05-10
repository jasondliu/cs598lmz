import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class W(ctypes.Structure):
    _fields_ = [("s", S)]

s = S()
w = W(s)
w.s == s  # True
