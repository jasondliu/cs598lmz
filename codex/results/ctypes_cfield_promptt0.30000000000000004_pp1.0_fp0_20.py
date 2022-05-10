import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class D(C):
    _fields_ = [("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int)]

    def __init__(self, a, b, c, d, e, f):
        C.__init__(self, a, b, c)
        self.d = d
        self.e = e
        self.f = f

class E(D):
    _fields_ = [("g", ctypes.c_int),
                ("h", ctypes.c_int),
                ("i", ctypes.c_int)]

    def __init__(self, a, b, c
