import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('s', S)]

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('b', ctypes.c_byte), ('s', S), ('z', ctypes.c_byte)]
    _pack_ = 1

class X(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('s', S)]

class B(ctypes.Structure):
    _fields_ = [('a', A), ('c', C), ('x', ctypes.c_int), ('u', X)]
    _pack_ = 1

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('b', c
