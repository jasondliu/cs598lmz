import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(C):
    _fields_ = C._fields_ + [('y', ctypes.c_int)]

d = D()
d.x = 42
d.y = 43

print d.x, d.y
