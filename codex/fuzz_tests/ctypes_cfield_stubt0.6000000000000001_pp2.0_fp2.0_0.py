import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__module__ = 'ctypes'

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]
S._fields_ = [('x', ctypes.c_int),
              ('y', ctypes.c_int)]

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
class Y(X):
    _fields_ = [('y', ctypes.c_int)]

import _ctypes_test
lib = ctypes.CDLL(_ctypes_test.__file__)

lib.my_callback.restype = ctypes.c_int
lib.my_callback.argtypes = (ctypes.c_int, ctypes.c_int)

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

X._fields_ = [('x', ctypes.c_int)]

class X(ct
