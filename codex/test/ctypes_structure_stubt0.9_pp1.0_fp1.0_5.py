import ctypes

class S(ctypes.Structure):
    x = [1, 2]
S._fields_ = [('X', ctypes.c_short*len(S.x))]
