import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    pass

class Y(ctypes.c_int):
    pass

class Z(ctypes.c_int):
    pass

class P(ctypes.Structure):
    _fields_ = [('x', X), ('y', Y), ('z', Z)]

class Q(ctypes.Structure):
    _fields_ = [('x', X), ('y', Y), ('z', Z)]

class R(ctypes.Structure):
    _fields_ = [('x', X), ('y', Y), ('z', Z)]

class S(ctypes.Structure):
    _fields_ = [('x', X), ('y', Y), ('z', Z)]

class T(ctypes.Structure):
    _fields_ = [('x', X), ('y', Y), ('z', Z)]

class U(ctypes.Structure):
    _fields_ = [('x', X), ('y', Y), ('z', Z)]

class V(ctypes.Structure):

