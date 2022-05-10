import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', ctypes.c_int)]

class W(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', ctypes.c_int)]

class V(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', ctypes.c_int)]

class U(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', ctypes.c_int)]

class S(
