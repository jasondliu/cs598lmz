import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
class CField(ctypes.CField):
    def __new__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        return super(CField, cls).__new__(cls, *args, **kwargs)

ctypes.CField = CField

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
</code>

