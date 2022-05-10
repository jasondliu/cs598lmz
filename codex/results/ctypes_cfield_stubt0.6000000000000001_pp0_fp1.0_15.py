import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, size):
        self.size = size

    def __getitem__(self, index):
        if not isinstance(index, ctypes.CField):
            raise TypeError("C indices must be ctypes.CFields")
        return self.size * index.offset

c = C(42)
print c[S.x]
print c[S.y]
</code>

