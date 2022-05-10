import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char), ('b', A)]

print(B.b.a)
