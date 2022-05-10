import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.CField):
    def __get__(self, obj, objtype=None):
        return ctypes.c_int.__get__(self, obj, objtype)

class S(ctypes.Structure):
    _fields_ = [('x', X)]

s = S()
s.x = 42
print repr(s.x)
</code>

