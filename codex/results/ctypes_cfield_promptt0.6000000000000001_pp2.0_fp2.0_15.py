import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

# Test ctypes.Field
class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]
    a = ctypes.Field(ctypes.c_int, 1, 2)
    b = ctypes.Field(ctypes.c_int, 1, 2)
    c = ctypes.Field(ctypes.c_int, 1, 2)
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

# Test ctypes.Union
class E(ctypes.Union):
    _fields_ = [("a
