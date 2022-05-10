import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField(C, "a"))]

d = D()
d.a = 1
d.b = 2
d.c = 3
print d.a, d.b, d.c

# Test ctypes.CField with offset
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField(C, "a", 1))]

e = E()
e.a = 1
e.b = 2
e.c = 3
print e.a, e.b, e.c

# Test ctypes.CField with offset and bits
class F(
