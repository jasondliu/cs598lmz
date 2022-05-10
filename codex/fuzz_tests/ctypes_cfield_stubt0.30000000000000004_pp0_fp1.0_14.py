import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    def __init__(self):
        self.x = 1

class Y(object):
    def __init__(self):
        self.x = 1

class Z(object):
    def __init__(self):
        self.x = 1

class A(object):
    def __init__(self):
        self.x = 1

class B(object):
    def __init__(self):
        self.x = 1

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


