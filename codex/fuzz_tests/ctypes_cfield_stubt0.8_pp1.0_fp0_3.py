import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.c_int):
    def from_param(cls, obj):
        return ctypes.c_int.from_param(cls, obj)
    from_param = classmethod(from_param)

S.x = C

s = S(42)
assert s.x == 42
</code>

