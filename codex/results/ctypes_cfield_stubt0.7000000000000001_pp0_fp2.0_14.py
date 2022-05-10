import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x

assert C(42) == C(42)
assert C(42) != C(43)

CField = ctypes.CField
cf = CField(None, C, 'x')

c = C(42)
assert cf.get(c) == 42
cf.set(c, 43)
assert cf.get(c) == 43
assert c.x == 43

assert c == C(43)
assert c != C(42)

#

class C:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x

CField = ctypes.CField
cf = CField(None, C, 'x')

c = C(42)
assert cf.get(c) == 42
cf.set(c, 43)
assert cf.get
