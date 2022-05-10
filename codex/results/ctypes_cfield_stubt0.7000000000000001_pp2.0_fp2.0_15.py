import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Subclassable(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('a', ctypes.c_byte),
                ('b', ctypes.c_byte)]

class Subclassed(Subclassable):
    _fields_ = [
        ('c', ctypes.c_int)
    ]

class A(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('x', ctypes.c_byte),
                ('y', ctypes.c_byte)]

class B(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('a', A),
                ('b', ctypes.c_byte)]

class C(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('a', A),
                ('b', ctypes.c_byte)]

class D(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('a', A), ('b', B)]

class E(ctypes
