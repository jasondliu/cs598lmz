import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    __slots__ = ['foo']
    def __init__(self):
        self.foo = 'bar'

    def __getattribute__(self, name):
        if name == 'foo':
            return 42

class C2(object):
    __slots__ = ['foo']
    def __init__(self):
        self.foo = 'bar'

class D(object):
    __slots__ = ['foo']
    def __init__(self):
        self.foo = 'bar'
    def meth(self):
        pass

class D2(object):
    __slots__ = ['foo']
    def __init__(self):
        self.foo = 'bar'
    def meth(self):
        pass

class X(object):
    def __getattribute__(self, name):
        return 42

class X2(object):
    def __getattribute__(self, name):
        return 42

def f():
    return 'abc'

def f2():
    return 'abc
