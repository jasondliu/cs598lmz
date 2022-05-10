import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print C.x
print S.x
print C.x == S.x
print C.x is S.x
print C.x.__class__
print S.x.__class__
print C.x.__class__ is S.x.__class__
print C.x.__class__ == S.x.__class__
print C.x.__class__ is ctypes.CField
print C.x.__class__ == ctypes.CField
print C.x.__class__ is ctypes.Field
print C.x.__class__ == ctypes.Field
