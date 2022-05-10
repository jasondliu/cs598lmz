import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(E.x)
print(D.x)
print(C.x)
print(S.x)
