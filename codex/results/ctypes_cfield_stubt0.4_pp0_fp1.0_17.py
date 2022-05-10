import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class Y(X):
    _fields_ = [('b', ctypes.c_int)]

class Z(Y):
    _fields_ = [('c', ctypes.c_int)]

class XX(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class YY(ctypes.Structure):
    _fields_ = [('b', ctypes.c_int)]

class ZZ(ctypes.Structure):
    _fields_ = [('c', ctypes.c_int)]

class XXX(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class YYY(ctypes.Structure):
    _fields_ = [('b', ctypes.c_int)]

class ZZZ(ctypes.Structure):
    _fields_ = [('c', ctypes.c_int)]

class X1(ct
