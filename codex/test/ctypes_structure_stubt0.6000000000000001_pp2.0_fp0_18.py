import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

class T(ctypes.Union):
    _fields_ = [('s', S), ('a', ctypes.c_double * 2)]

x = T()
x.a[0] = 1.0
x.a[1] = 2.0
print(x.s.x, x.s.y)
x.s.x = 3.0
print(x.a[0], x.a[1])
