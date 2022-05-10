import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __init__(self, v):
        self.v = v
    def _get_value(self):
        return self.v
    def _set_value(self, v):
        self.v = v
    value = property(_get_value, _set_value)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', C(42))]

x = X()
x.b
x.b = 1
x.b

x.a
x.a = 1
x.a

S.x.__get__(S())
