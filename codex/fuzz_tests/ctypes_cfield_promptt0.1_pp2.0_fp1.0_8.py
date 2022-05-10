import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField(C, "a", "b"))]

d = D()
d.a = 1
d.b = 2
print d.c.a, d.c.b
d.c.a = 3
d.c.b = 4
print d.a, d.b

# Test ctypes.CField with offset
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField(C, "a", "b", 1))]

e = E()
e.a = 1
e.b = 2
print e.c.a, e.c
