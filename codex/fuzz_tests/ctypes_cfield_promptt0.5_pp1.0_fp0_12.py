import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]
    def __init__(self, a):
        self.a = a

class Y(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Z(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class W(ctypes.Union):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z)]

class U(ctypes.Union):
    _fields_ = [('x',
