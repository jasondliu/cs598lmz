import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __init__(self, *args):
        self.__dict__['_fields_'] = args

    def __setattr__(self, name, value):
        self._fields_.append((name, value))

    def __getattr__(self, name):
        return [x for x in self._fields_ if x[0] == name][0][1]
</code>

