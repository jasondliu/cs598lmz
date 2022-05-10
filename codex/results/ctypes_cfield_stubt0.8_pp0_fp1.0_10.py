import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('a1', ctypes.c_int), ('a2', ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [('b1', ctypes.c_int), ('b2', ctypes.c_double), ('b3', A)]

class C(ctypes.Structure):
    _fields_ = [('c1', ctypes.c_int), ('c2', ctypes.c_double), ('c3', A), ('c4', B)]

class D(ctypes.Structure):
    _fields_ = [('d1', ctypes.c_int), ('d2', ctypes.c_double),
                ('d3', A), ('d4', B), ('d5', C)]

class E(ctypes.Structure):
    _fields_ = [('e1', ctypes.c_int), ('e2', ctypes.c_double),
                ('e3', A), ('e4', B), ('e5
