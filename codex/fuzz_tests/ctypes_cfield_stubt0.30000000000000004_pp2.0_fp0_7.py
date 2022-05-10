import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __init__(self, *args, **kw):
        super(CField, self).__init__(*args, **kw)
        self.name = 'CField'

class S2(ctypes.Structure):
    _fields_ = [('x', CField)]

print(S2.x.name)
</code>
Output:
<code>CField
</code>

