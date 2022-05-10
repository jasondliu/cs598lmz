import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    pass

c = C()
c.x = 42

assert isinstance(c.x, ctypes.CField)
assert ctypes.CField(42) == 42
assert ctypes.CField() == 0
assert ctypes.CField(c.x) == 42
assert ctypes.CField(c.x) != 24
assert ctypes.CField(24).value == 24
assert ctypes.CField(c.x).value == 42
assert S(c.x).x == 42
assert S(ctypes.CField(42)).x == 42
