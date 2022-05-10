import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __getattr__(self, name):
        return ctypes.CField(name)

print(C().x)
</code>
Output:
<code>_CField(name='x')
</code>

