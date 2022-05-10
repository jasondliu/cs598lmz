import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(ctypes.c_int, 0))]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(ctypes.c_int, 0, True))]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(ctypes.c_int, 0, True, True))]

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(ctypes.c_int, 0, False, False))]

assert isinstance(C.x, ctypes.CField)
assert isinstance(D.x, ctypes.CField)
assert isinstance(E.x, ctypes.CField)
assert isinstance(T.x, ctypes.CField)

assert not C.x.is_volatile
assert D.x.is_volatile
assert E.x.is_volatile
assert not T
