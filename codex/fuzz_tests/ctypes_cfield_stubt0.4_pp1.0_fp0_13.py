import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    def __getattribute__(self, name):
        if name == 'x':
            return 42
        return super(X, self).__getattribute__(name)

class Y(X):
    x = ctypes.CField()

print Y().x
