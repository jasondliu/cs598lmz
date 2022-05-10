import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__doc__ = 'doc'

class S(ctypes.Structure):
    _fields_ = [('x', CField(ctypes.c_int))]

print(S.x.__doc__)
</code>
Output:
<code>doc
</code>

