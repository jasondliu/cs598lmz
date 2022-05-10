import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

c = C(1)
s = S.from_address(id(c))
assert s.x == 1
del c
assert s.x == 1
s.x = 42
c = C(0)
assert s.x == 1
s = S.from_address(id(c))
assert s.x == 42
