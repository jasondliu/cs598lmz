import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z)]

class E(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z)]

class F(ctypes.Structure):
    _fields_ = [('x', X),
               
