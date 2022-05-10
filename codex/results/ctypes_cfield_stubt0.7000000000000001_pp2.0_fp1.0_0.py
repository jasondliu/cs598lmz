import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __getitem__(self, i):
        assert isinstance(i, ctypes.CField)
        return i.value

c = C()
c.x = 42
assert c[c.x] == 42
assert c[C.x] == 42
