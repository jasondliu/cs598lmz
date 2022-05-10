import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(ctypes.Structure):
    _fields_ = [("s", S)]

a = A()
a.s.x = 1
