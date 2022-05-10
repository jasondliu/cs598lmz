import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class B(ctypes.Structure):
    _fields_ = [("s", S)]

class C(ctypes.Structure):
    _fields_ = [("b", B)]

class D(ctypes.Structure):
    _fields_ = [("c", C)]

class E(ctypes.Structure):
    _fields_ = [("d", D)]

a = E()
a.d.c.b.s.x = 2

b = a.d.c.b
b.s.x = 3

print(a.d.c.b.s.x)
