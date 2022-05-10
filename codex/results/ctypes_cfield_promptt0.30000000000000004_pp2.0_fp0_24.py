import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C)]

class E(ctypes.Structure):
    _fields_ = [("d", D)]

class F(ctypes.Structure):
    _fields_ = [("e", E)]

f = F()
f.e.d.c.a = 1
f.e.d.c.b = 2

print f.e.d.c.a, f.e.d.c.b

f.e.d.c = C(3, 4)

print f.e.d.c.a, f.e.d.c.b

f.e.d.c = (5, 6)

print f.e.d.c.a, f.e.d.c.b

f.e.d.c = [7, 8]

print f.
