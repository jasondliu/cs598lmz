import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert isinstance(S.x, ctypes.CField)
assert issubclass(ctypes.CField, ctypes.Field)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

assert S.x is not S2.x
s1 = S()
s2 = S2()
assert s1.x is s2.x
assert s1.x.__class__ is ctypes.c_int
assert s2.x.__class__ is ctypes.c_int
print('---')

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self, x=None):
        super(S, self).__init__()
        if x is not None: self.x = x

s = S()
assert s.x == 0
print(s.x)
s = S(1)
assert s.x == 1
print(s.x)

class S(ctypes.Structure):

