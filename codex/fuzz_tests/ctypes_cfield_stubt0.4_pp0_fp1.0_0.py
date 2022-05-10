import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self, value):
        self.x = value

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self, value):
        self.x = value

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self, value):
        self.x = value

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self, value):
        self.x = value

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self, value):
        self.x = value

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c
