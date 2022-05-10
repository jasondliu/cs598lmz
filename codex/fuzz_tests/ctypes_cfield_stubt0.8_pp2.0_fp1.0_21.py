import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.CField, ctypes.c_char):
    _type_ = 'B'

class D(C):
    _type_ = 'b'

class E(C):
    _type_ = 'c'

# x is supposed to not be a character type:
class X(C, ctypes.c_int):
    _type_ = 'i'

for cls in (C, D, E):
    s = S()
    s.x = cls(b'\x12')
    assert s.x == 0x12
    s.x = cls(b'\x34')
    assert s.x == 0x34

s = S()
s.x = X(0x12)
assert s.x == 0x12
s.x = X(0x34)
assert s.x == 0x34
