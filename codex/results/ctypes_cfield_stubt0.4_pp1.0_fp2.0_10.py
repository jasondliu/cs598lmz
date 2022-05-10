import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __init__(self, *args, **kw):
        self.__dict__.update(kw)
        super().__init__(*args)

class S(ctypes.Structure):
    _fields_ = [('x', CField(ctypes.c_int, foo=42))]

print(S.x.foo)
</code>
Output:
<code>42
</code>

