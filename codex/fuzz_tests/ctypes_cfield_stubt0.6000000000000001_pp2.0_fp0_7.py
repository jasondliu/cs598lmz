import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(ctypes.CField)
print(ctypes.CField.__name__)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

ctypes.CField = type(S.x)
print(ctypes.CField)
print(ctypes.CField.__name__)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__name__ = "myint"
print(ctypes.CField)
print(ctypes.CField.__name__)
