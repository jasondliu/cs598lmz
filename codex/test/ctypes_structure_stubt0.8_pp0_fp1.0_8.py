import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class Arr(ctypes.Structure):
    _fields_ = [('n', ctypes.c_int), ('arr', ctypes.POINTER(S))]

