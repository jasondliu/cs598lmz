import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int)]

d = D()
d.c.a = 1
d.c.b = 2
d.d = 3

print d.c.a, d.c.b, d.d

d.c = C(4, 5)
print d.c.a, d.c.b, d.d

d.c = C(a=6, b=7)
print d.c.a, d.c.b, d.d

d.c = C(b=8, a=9)
print d.c.a, d.c.b, d.d

d.c = C(10, b=11)
print d.c.a, d.c.b, d.d

d.c = C(b
