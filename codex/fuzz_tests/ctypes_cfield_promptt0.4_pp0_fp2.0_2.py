import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

    def __init__(self):
        super(C, self).__init__()
        self.a = 1
        self.b = 2

class D(C):
    _fields_ = [("c", ctypes.c_int),
                ("d", ctypes.c_int)]

    def __init__(self):
        super(D, self).__init__()
        self.c = 3
        self.d = 4

class E(D):
    _fields_ = [("e", ctypes.c_int),
                ("f", ctypes.c_int)]

    def __init__(self):
        super(E, self).__init__()
        self.e = 5
        self.f = 6

class F(E):
    _fields_ = [("g", ctypes.c_int),
                ("h", ctypes.c_int)]

    def
