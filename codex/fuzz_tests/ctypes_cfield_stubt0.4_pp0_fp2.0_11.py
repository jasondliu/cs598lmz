import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

class D(C):
    def __init__(self):
        C.__init__(self)
        self.y = 2

class E(D):
    def __init__(self):
        D.__init__(self)
        self.z = 3

class F(E):
    def __init__(self):
        E.__init__(self)
        self.t = 4

class G(F):
    def __init__(self):
        F.__init__(self)
        self.u = 5

class H(G):
    def __init__(self):
        G.__init__(self)
        self.v = 6

class I(H):
    def __init__(self):
        H.__init__(self)
        self.w = 7

class J(I):
    def __init__(self):
        I.__init__(self)
        self.x = 8

