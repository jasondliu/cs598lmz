import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

class D(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

class C(ctypes.Structure):
    _fields_ = [("s", S), ("d", D)]

class C2(ctypes.Structure):
    _fields_ = [("s", S), ("d", D)]

class C3(ctypes.Structure):
    _fields_ = [("s", S), ("d", D)]

