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
    def __getattribute__(self, name):
        if name == 'x':
            return 42
        else:
            return object.__getattribute__(self, name)

class F(object):
    def __init__(self, x):
        self.x = x
    def __getattribute__(self, name):
        if name == 'x':
            return 42
        else:
            return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == 'x':
            raise AttributeError("can't set attribute")
        else:
            return object.__setattr__(self, name, value)

class G(object):
    def __init__(self, x
