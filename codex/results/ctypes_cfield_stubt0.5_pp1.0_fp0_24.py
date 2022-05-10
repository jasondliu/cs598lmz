import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class M(type):
    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        return self.__dict__[name]

class C(metaclass=M):
    def __init__(self, *args):
        self.args = args

    def __call__(self, *args):
        return self.args + args

    def __getitem__(self, item):
        return item

class D(metaclass=M):
    def __init__(self, *args):
        self.args = args

    def __call__(self, *args):
        return self.args + args

    def __getitem__(self, item):
        return item

    def __getattr__(self, item):
        return item

class E(metaclass=M):
    def __init__(self, *args):
        self.args = args

    def __call__(self, *args):
        return self.args + args

    def __getitem
