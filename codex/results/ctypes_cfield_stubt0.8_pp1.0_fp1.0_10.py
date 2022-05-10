import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class R(ctypes.CField):
    _type_ = ctypes.c_int
    _name_ = 'x'
    _offset_ = 0
    _index_ = 0

f = R()
assert f.__class__ == ctypes.CField
assert isinstance(f, ctypes.c_int)
assert f._type_ is ctypes.c_int
assert f._name_ == 'x'
assert f._offset_ == 0
assert f._index_ == 0
try:
    f.x # should still be an int
except AttributeError:
    pass
else:
    print('bug in types.py')

class RR(ctypes.Structure):
    _fields_ = [('x', R)]

s = RR()

assert isinstance(s.x, R)
assert s.x.__class__ == R

s.x = 42
assert s.x == 42
assert isinstance(s.x, R)
assert s.x.__class__ == R

s = RR()

s.x = R
