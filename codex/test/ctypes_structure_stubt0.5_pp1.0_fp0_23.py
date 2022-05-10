import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

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
