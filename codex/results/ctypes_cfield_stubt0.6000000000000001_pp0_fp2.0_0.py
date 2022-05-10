import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return ctypes.CField.__get__(self, obj, objtype)

    def __set__(self, obj, value):
        ctypes.CField.__set__(self, obj, value)
        # print the new value
        print 'new value is', ctypes.CField.__get__(self, obj)

S.x = CField(('x', ctypes.c_int))

s = S(5)
s.x = 6
</code>

