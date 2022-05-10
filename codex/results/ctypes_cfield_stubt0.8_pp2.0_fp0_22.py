import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(S.x._type_)
print(S.x._name_)
print(S.x._offset_)
