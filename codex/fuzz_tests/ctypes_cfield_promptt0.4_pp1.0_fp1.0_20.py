import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int)]

d = D(C(1, 2), 3)
print(d.c.a, d.c.b, d.d)
print(d.c)
print(d)

# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int)]

d = D(C(1, 2), 3)
print(d.c.a, d.c.b, d.d)
print(d.c)
print(d)

# Test ctypes.CField
