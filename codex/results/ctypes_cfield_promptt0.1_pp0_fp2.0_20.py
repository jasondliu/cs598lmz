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
print d.c
d.c = 3
print d.a, d.b

# Test ctypes.CField.from_address
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField.from_address(ctypes.addressof(d), "a", "b"))]

e = E()
print e.c
e.c = 4
print d.a, d.b

# Test ctypes.CField.
