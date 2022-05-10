import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    def __init__(self):
        self.a = 1
        self.b = 2

x = X()
print(x.a, x.b)

# Test ctypes.CField
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

y = Y()
print(y.a, y.b, y.c)

# Test ctypes.CField
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", c
