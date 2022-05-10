import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    @ctypes.cfield(S.x)
    def foo(self):
        return 42

print(C().foo)
</code>
The output:
<code>42
</code>

