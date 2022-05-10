import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

class D(object):
    def __init__(self):
        self.x = 1

class E(object):
    def __init__(self):
        self.x = 1

class F(object):
    def __init__(self):
        self.x = 1

class G(object):
    def __init__(self):
        self.x = 1

class H(object):
    def __init__(self):
        self.x = 1

class I(object):
    def __init__(self):
        self.x = 1

class J(object):
    def __init__(self):
        self.x = 1

class K(object):
    def __init__(self):
        self.x = 1

class L(object):
    def __init__(self):
        self.x = 1

class M(object):
    def __init__(self):
        self.x = 1


