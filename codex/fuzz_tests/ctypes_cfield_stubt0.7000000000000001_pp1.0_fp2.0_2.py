import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    __dict__ = property(lambda self: self.__dict__)
    __class__ = property(lambda self: self.__class__)

class C2(object):
    def __init__(self):
        self.x = 0

    __dict__ = property(lambda self: self.__dict__)
    __class__ = property(lambda self: self.__class__)

class C3(object):
    def __init__(self):
        self.x = 0

    __dict__ = property(lambda self: self.__dict__)

class C4(object):
    def __init__(self):
        self.x = 0

    __class__ = property(lambda self: self.__class__)

class C5(object):
    def __init__(self):

