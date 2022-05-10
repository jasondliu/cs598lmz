import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(S))]

assert isinstance(C.p, ctypes.CField)
assert isinstance(C.p.__ctype__, ctypes.CField)
assert isinstance(C.p.__ctype__.__ctype__, ctypes.CField)
assert isinstance(C.p.__ctype__.__ctype__.__ctype__, ctypes.CField)
assert C.p.__ctype__.__ctype__.__ctype__.__ctype__ is None

assert C.p._type_ == 'P'
assert C.p.__ctype__._type_ == 'i'
assert C.p.__ctype__.__ctype__._type_ == 'i'
assert C.p.__ctype__.__ctype__.__ctype__._type_ == 'i'
assert C.p.__ctype__.__ctype__.__ctype__.__ctype__ is None

