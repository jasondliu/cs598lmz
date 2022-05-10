import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __setattr__(self, name, value):
        if not hasattr(self, name):
            raise AttributeError("'%s' object has no attribute '%s'" %
                                 (self.__class__.__name__, name))
        if isinstance(value, ctypes.CField):
            raise ValueError("can't assign to '%s' (c field)" % name)
        object.__setattr__(self, name, value)

class D(C, ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class F(E, C):
    pass

def bug(x):
    print("bug in ", x, file=sys.stderr)
    sys.exit(1)

s = S()
s.x = 42
s.x = 43
s.xx = 44
try:
    s.xx = 45

