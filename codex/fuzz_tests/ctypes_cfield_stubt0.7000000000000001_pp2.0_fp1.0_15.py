import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(S.x)
print(S._fields_[0])
print(ctypes.CField)
print(type(S._fields_[0]) == ctypes.CField)
