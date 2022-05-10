import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(S))]

t = T()

