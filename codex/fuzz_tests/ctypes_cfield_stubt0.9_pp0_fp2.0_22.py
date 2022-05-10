import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
for f in S._fields_:
    assert type(f[1] is ctypes.CField)
