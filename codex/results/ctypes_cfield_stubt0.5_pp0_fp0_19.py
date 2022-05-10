import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

C._fields_ = [('x', ctypes.c_int)]

# This will segfault on CPython
C._fields_ = []

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

D._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

# This will segfault on CPython
D._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 3)]

E._fields_ = [('x', ctypes.c_int * 3)]

# This will segfault on CPython
E._fields_ = [('x', ctypes.c_int * 3), ('y', c
