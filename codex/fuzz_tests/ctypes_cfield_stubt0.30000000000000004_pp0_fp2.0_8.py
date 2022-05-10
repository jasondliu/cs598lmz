import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __init__(self):
        self.x = 1

class D(C):
    pass

class E(C):
    def __init__(self):
        self.x = 1

class F(C):
    def __init__(self):
        self.x = 1
    def __getattr__(self, name):
        return 42

class G(C):
    def __getattr__(self, name):
        return 42

class H(C):
    def __getattr__(self, name):
        return 42
    def __setattr__(self, name, value):
        pass

class I(C):
    def __setattr__(self, name, value):
        pass

class J(C):
    def __setattr__(self, name, value):
        pass
    def __getattr__(self, name):
        return 42

class K(C):
    def __getattr__(self, name):
        return 42
    def __setattr__(self, name,
