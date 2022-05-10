import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

assert isinstance(S.x, ctypes.c_int)
assert S.x.__class__ is ctypes.c_int

s = S()
assert isinstance(s.x, ctypes.c_int)
assert s.x.__class__ is ctypes.c_int

assert s.x is s.x

assert s.x == 0

assert repr(s.x) == 'c_int(0)'

s.x = 1
assert s.x == 1

s.x += 1
assert s.x == 2

assert str(s.x) == '2'
assert type(str(s.x)) is str

assert hex(s.x) == '0x2'
assert type(hex(s.x)) is str

assert ord(s.x) == 2
assert type(ord(s.x)) is int

assert hash(s.x) == 2
assert type(hash(s.x)) is int

assert abs(s.x) == 2
assert type(abs
