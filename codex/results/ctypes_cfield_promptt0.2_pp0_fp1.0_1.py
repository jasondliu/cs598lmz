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

d.c.a = 5
print d.c.a, d.c.b, d.d

d.d = 6
print d.c.a, d.c.b, d.d

d.c = C(7, 8)
print d.c.a, d.c.b, d.d

d.c = C(9, 10)
print d.c.a, d.c.b, d.d

d.d = 11
print d.c.a, d.c.b, d.d

d
