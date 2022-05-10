import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 1

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 1
    def __del__(self):
        pass

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 1
    def __del__(self):
        pass
    def __repr__(self):
        return "G"

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 1
