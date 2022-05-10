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
    def __getattr__(self, name):
        if name == 'x':
            return self.__dict__['x']
        raise AttributeError

class E(object):
    def __init__(self, x):
        self.x = x
    def __getattribute__(self, name):
        if name == 'x':
            return self.__dict__['x']
        raise AttributeError

class F(object):
    def __init__(self, x):
        self.x = x
    def __getattribute__(self, name):
        if name == 'x':
            return self.__dict__['x']
        return object.__getattribute__(self, name)

class G(object):
    def __init__(self, x):
        self.x = x
    def __getattribute__(self, name
