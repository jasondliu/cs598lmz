import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __setattr__(self, attr, value):
        if attr in self._fields_:
            ctypes.CField.__setattr__(self.x, attr, value)
        else:
            ctypes.Structure.__setattr__(self, attr, value)

c = C()
c.x.value = 42

print(c.x)
</code>

