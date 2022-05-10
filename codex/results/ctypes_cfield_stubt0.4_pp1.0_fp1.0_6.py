import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._offset = 0

S._fields_ = [('x', CField(ctypes.c_int))]
print(S.x)
</code>
Output:
<code>&lt;Field type=c_int, ofs=0, size=4&gt;
</code>

