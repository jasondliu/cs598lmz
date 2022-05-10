import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class B(object):
    pass

assert type(B.x) is not ctypes.CField
B.x = ctypes.c_int
assert type(B.x) is ctypes.CField

class C(type):
    def __new__(cls, name, bases, dict):
        dict['x'] = ctypes.c_int
        return type.__new__(cls, name, bases, dict)

class D(object):
    __metaclass__ = C

assert type(D.x) is ctypes.CField
