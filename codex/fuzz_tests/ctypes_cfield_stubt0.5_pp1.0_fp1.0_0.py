import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class C2(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class C3(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print S.x.__class__
print S.x.__class__ is ctypes.CField
print C.x.__class__ is ctypes.CField
print C2.x.__class__ is ctypes.CField
print C3.x.__class__ is ctypes.CField
print D.x.__class__ is ctypes.CField

print S.x.__class__ is C.x.__class__
print C.x.__class__ is C2.x.__class__
print C2.x.__class__ is C3.x.__class__
print C
