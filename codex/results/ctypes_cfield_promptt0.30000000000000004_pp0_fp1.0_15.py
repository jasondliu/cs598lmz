import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    def __init__(self):
        self.a = 1
        self.b = 2

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int)]
    def __init__(self):
        self.c.a = 1
        self.c.b = 2
        self.d = 3

d = D()
print(d.c.a, d.c.b, d.d)

# Test ctypes.CArray
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int * 2)]
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c[0] = 3
        self.c
