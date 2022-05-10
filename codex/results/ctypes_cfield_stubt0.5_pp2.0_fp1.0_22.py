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

class A(ctypes.Union):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z)]

A._pack_ = 4

class B(ctypes.Union):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z)]

class C(ctypes.Union):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z)]

C._pack_ = 1

class D(ctypes.Union):

