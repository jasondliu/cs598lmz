import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

assert isinstance(S.x, ctypes.c_int)
assert S.x.__class__ is ctypes.c_int

s = S()
assert isinstance(s.x, ctypes.c_int)
assert s.x.__class__ is ctypes.c_int

assert s.x is s.x

