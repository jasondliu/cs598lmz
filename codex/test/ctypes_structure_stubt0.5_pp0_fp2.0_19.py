import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class X(ctypes.Structure):
    _fields_ = [('a', S), ('b', S)]

x = X()
