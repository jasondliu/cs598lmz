import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def make_readonly(field):
    assert isinstance(field, ctypes.CField)
    def fget(self):
        return getattr(self, field.name)
    def fset(self, value):
        raise RuntimeError("readonly")
    return property(fget, fset, None, None)

class S2(S):
    x = make_readonly(S.x)

s = S2()
s.x = 1
print s.x
s.x = 2
</code>

