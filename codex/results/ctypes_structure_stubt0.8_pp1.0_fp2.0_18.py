import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

class T(ctypes.Structure):
    a = ctypes.c_int
    b = S
    c = ctypes.c_int

t = T()
t.a = 1
t.b.x = 2.0
t.c = 3

print t.a, t.b.x, t.c

addr = ctypes.addressof(t)
s = ctypes.cast(addr, ctypes.POINTER(T))

print s.contents.a, s.contents.b.x, s.contents.c
