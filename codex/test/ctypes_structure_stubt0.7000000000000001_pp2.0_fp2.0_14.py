import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class C(ctypes.Structure):
    _fields_ = [('val', S)]

c = C()
