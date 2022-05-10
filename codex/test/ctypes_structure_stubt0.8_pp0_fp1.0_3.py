import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

    def __init__(self, **kw):
        self.__setattr__('x', 5)

class Foo(object):
    x = 0
    def __init__(self, **kw):
        self.__setattr__('x', 5)

c = Foo(x=3)

