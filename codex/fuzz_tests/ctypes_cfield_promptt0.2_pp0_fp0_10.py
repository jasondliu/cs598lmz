import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(C, "a", ctypes.c_int))]

d = D()
d.a = 1
d.b = 2
print(d.b)

# Test ctypes.CField with offset
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(C, "a", ctypes.c_int, 1))]

e = E()
e.a = 1
e.b = 2
print(e.b)

# Test ctypes.CField with offset and size
class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(
