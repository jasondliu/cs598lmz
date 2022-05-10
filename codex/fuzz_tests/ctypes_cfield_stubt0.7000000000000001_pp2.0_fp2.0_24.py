import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int),
                ('s', S),
                ('z', ctypes.c_int)]

class N(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    _pack_ = 1

class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int),
                ('c', ctypes.c_int * 2)]

class B(ctypes.Structure):
    _fields_ = [('d', ctypes.c_char * 4), ('e', ctypes.c_int)]

class AB(ctypes.Structure):
    _fields_ = [('ab', A), ('b', B)]

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_byte)]

class Y(ctypes.Structure):
    _fields
