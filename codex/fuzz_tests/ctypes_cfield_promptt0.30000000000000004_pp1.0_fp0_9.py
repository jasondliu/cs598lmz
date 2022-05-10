import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", ctypes.CField(C, "a")),
                ("d", ctypes.CField(C, "b"))]

c = C(1, 2)
d = D.from_address(ctypes.addressof(c))
print(d.c, d.d)

# Test ctypes.CField with a pointer
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [("c", ctypes.POINTER(E)),
                ("d", ctypes.CField(E, "a")),
                ("e", ctypes.CField(E, "b"))]

e = E(1, 2)
f = F
