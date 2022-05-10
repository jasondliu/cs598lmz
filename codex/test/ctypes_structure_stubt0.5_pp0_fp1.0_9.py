import ctypes

class S(ctypes.Structure):
    x = 0

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", S)]

class X(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(D))]

x = X()
print(x.p)
