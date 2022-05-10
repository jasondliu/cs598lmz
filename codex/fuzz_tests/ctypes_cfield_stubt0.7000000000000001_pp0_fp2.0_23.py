import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert (ctypes.CField == type(S.x))
    assert (type(ctypes.CField) == type)
    assert (isinstance(S.x, ctypes.CField))
    assert issubclass(ctypes.CField, ctypes.Field)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_int)

import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class Y(X):
    _fields_ = X._fields_ + [('b', ctypes.c_int)]

try:
    class Y(X):
        _fields_ = X._fields_ + [('b', ctypes.c_int), ('a', ctypes.c_int)]
except ValueError:
    pass
else:
    raise RuntimeError

try:
    class Y(X):
        _fields_ =
