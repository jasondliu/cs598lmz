import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __getattribute__(self, name):
        if name == 'x':
            return 42
        else:
            return object.__getattribute__(self, name)

s = S()
s.x = C()
print s.x
