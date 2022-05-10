import ctypes

class S(ctypes.Structure):
    x = ctypes.c_wchar
    def func(self): return 1
    def __str__(self): return 'in S'


class FOO(object):
    _x = None
    @property
    def x(self):
        if self._x is None:
            self._x = S()
        return self._x

    def __str__(self): return 'in foo'
    def __repr__(self): return "FOO()"
