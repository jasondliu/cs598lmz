import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
for x in S._fields_:
    print x
    print type(x)
    print S.x
    print type(S.x)
