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
print(d.a, d.b, d.c)

# Test ctypes.CField.from_address
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField.from_address(ctypes.addressof(d), "a"))]

e = E()
e.a = 4
e.b = 5
e.c = 6
print(e.a, e.b, e.c)
print
