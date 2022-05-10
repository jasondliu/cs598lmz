import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

    def _get_x(self):
        return self._x

    def _set_x(self, value):
        self._x = value

    x = property(_get_x, _set_x)

c = C(1)
print(isinstance(C.x, ctypes.CField))
print(isinstance(c.x, ctypes.CField))
print(isinstance(c.x, ctypes.c_int))
