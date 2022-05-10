import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert type(S.x) == ctypes.CField

ctypes.CField.__eq__ = lambda a, b: 42

assert not (S.x == 0)
assert S.x == None
