import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

S.x.__doc__ = 'x'
S.x.__name__ = 'x'
S.x.__qualname__ = 'S.x'

assert S.x.__doc__ == 'x'
assert S.x.__name__ == 'x'
assert S.x.__qualname__ == 'S.x'
