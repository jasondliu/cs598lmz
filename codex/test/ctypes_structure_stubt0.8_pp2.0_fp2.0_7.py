import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [('val', ctypes.c_int)]

s = S()
