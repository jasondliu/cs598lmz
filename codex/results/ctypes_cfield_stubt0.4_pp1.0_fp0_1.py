import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 0

class D(C):
    _fields_ = [('y', ctypes.c_int)]
    def __init__(self):
        self.y = 0

class E(D):
    _fields_ = [('z', ctypes.c_int)]
    def __init__(self):
        self.z = 0

class F(E):
    _fields_ = [('w', ctypes.c_int)]
    def __init__(self):
        self.w = 0

class G(F):
    _fields_ = [('a', ctypes.c_int)]
    def __init__(self):
        self.a = 0

class H(G):
    _fields_ = [('b', ctypes.c_int)]
    def __init__(self):
        self.b = 0

class I(H):
    _fields
