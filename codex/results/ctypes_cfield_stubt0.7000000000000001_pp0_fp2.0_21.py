import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('f', S),
                ('g', ctypes.c_int),
                ('h', ctypes.c_int),
                ('i', ctypes.c_int),
                ('j', ctypes.c_int)]

a = A()
a.f.x = 1
print a.f.x, a.g, a.h, a.i, a.j
a.f = S(2)
print a.f.x, a.g, a.h, a.i, a.j
a.f = S(3)
print a.f.x, a.g, a.h, a.i, a.j
