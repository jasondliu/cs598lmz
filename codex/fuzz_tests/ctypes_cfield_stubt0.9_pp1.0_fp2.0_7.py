import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

f = S.x
assert f is S.x

print(f.__class__)
f.__class__ = ctypes.c_int32
S.x = ctypes.c_bool
assert S._fields_[0][1] == ctypes.c_bool

class R(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int8 * 3)]

assert R.x.__class__ is ctypes.CArrayType
assert R.x[0].__class__ is ctypes.c_int8

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 3)]

assert S.x.__class__ is ctypes.POINTER(ctypes.c_int)
assert S.x[0].__class__ is ctypes.c_int

class c_double_node(ctypes.Structure):
    _fields_ = [
        ("data", ctypes.c_double),
        ("next", ctypes.POINTER(ctypes.c
