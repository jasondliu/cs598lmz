import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint()

class T(ctypes.Structure):
    i = ctypes.c_uint

class U(ctypes.Structure):
    _fields_ = [("i", ctypes.c_uint)]

class V(ctypes.Structure):
    _fields_ = [("i", ctypes.c_uint)]
    _pack_ = 4

class X(ctypes.Structure):
    _fields_ = [("u", ctypes.Union)]

print(ctypes.sizeof(S))
print(ctypes.sizeof(T))
print(ctypes.sizeof(U))
print(ctypes.sizeof(V))
print(ctypes.sizeof(X))
