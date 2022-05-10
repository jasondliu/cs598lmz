import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, value):
        self.value = value
    def __get__(self, obj, type=None):
        return self.value
    def __set__(self, obj, value):
        self.value = value
    def __delete__(self, obj):
        raise AttributeError

class D(object):
    def __get__(self, obj, type=None):
        return obj
    def __set__(self, obj, value):
        raise AttributeError
    def __delete__(self, obj):
        raise AttributeError

class E(object):
    def __get__(self, obj, type=None):
        return obj
    def __set__(self, obj, value):
        raise AttributeError
    def __delete__(self, obj):
        raise AttributeError

class F(object):
    def __get__(self, obj, type=None):
        return obj
    def __set__(self, obj, value):
        raise AttributeError
    def
