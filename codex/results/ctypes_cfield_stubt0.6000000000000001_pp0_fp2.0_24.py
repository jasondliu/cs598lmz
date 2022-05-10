import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Structure):
    _fields_ = [('y', ctypes.c_double)]

s = S(42)
print(s.x)
print(s._fields_[0][1] is ctypes.c_int)
print(ctypes.CField(ctypes.c_double))
print(D.y.type is ctypes.c_double)
