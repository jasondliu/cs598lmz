import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
s = S()
s.x = 42
assert '<Field x of type c_long>' in repr(S.x)
assert '<CField x of type c_int>' in repr(s.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_long)]

assert type(s.x) is ctypes.CField
assert type(S.x) is not ctypes.CField
assert type(S2.x) is not ctypes.CField
