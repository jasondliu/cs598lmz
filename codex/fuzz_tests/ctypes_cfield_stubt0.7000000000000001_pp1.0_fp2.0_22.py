import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __new__(cls, *args, **kwargs):
        self = super(CField, cls).__new__(cls, *args, **kwargs)
        assert isinstance(self, ctypes.CField)
        print('CField.__new__:', self)
        return self

s = S(1)
print('s.x:', s.x)
