import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(D.x)
print(C.x is D.x)

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

print(C.x is E.x)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

print(E.x is F.x)
