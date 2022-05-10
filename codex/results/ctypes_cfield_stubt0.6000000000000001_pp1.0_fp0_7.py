import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

assert isinstance(C.x, ctypes.CField)
assert issubclass(C.x.__class__, ctypes.CField)
assert C.x.__class__ is ctypes.CField

assert C.x.__class__.__name__ == 'CField'
assert C.x.__class__.__module__ == 'ctypes'
