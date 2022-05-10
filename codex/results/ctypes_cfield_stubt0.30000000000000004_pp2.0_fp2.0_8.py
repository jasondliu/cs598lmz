import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class A(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z)]

class B(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z)]

class C(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z)]

class D(ctypes.Structure):
    _fields_ = [('a', A),

