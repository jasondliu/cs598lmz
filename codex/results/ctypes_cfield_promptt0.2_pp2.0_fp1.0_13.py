import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    def __init__(self):
        self.a = 1
        self.b = 2

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]
    def __init__(self):
        self.x.a = 3
        self.x.b = 4
        self.y = 5

y = Y()
print y.x.a, y.x.b, y.y

# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    def __init__(self):
        self.a = 1
        self.b = 2

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.
