import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

v = S._fields_[0]

print(v[0])
print(v[1])
print(v)

v[1] = ctypes.c_int

print(v)
print(v[1])

print(S._fields_)
