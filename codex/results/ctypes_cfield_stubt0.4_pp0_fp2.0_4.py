import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

    def __getattr__(self, name):
        if name == 'x':
            return self.__dict__[name]
        raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'x':
            self.__dict__[name] = value
            return
        raise AttributeError(name)

    def __repr__(self):
        return '<C %r>' % (self.x,)

class D(object):
    def __init__(self, x):
        self.x = x

    def __getattr__(self, name):
        if name == 'x':
            return self.__dict__[name]
        raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'x':
            self.__dict__[name] = value
            return
        raise AttributeError(name)

    def __repr__
