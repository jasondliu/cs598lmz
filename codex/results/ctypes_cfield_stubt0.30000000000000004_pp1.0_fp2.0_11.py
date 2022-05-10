import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

class D(object):
    def __init__(self, x):
        self.x = x

class E(object):
    def __init__(self, x):
        self.x = x

class F(object):
    def __init__(self, x):
        self.x = x

class G(object):
    def __init__(self, x):
        self.x = x

class H(object):
    def __init__(self, x):
        self.x = x

class I(object):
    def __init__(self, x):
        self.x = x

class J(object):
    def __init__(self, x):
        self.x = x

class K(object):
    def __init__(self, x):
        self.x = x

class L(object):
    def __init__(self, x):
        self.x = x

class M(
