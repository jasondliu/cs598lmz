import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    def __init__(self, x):
        self.x = x

class Y(object):
    def __init__(self, x):
        self.x = x

class Z(object):
    def __init__(self, x):
        self.x = x

class A(object):
    def __init__(self, x):
        self.x = x

class B(object):
    def __init__(self, x):
        self.x = x

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

class H(
