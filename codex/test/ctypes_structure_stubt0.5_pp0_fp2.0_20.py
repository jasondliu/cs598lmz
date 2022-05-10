import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int), ('x', ctypes.c_int)]

class N(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('x', ctypes.c_int)]

class M(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('x', ctypes.c_int)]
    x = ctypes.c_int
    x = ctypes.c_int

class O(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('x', ctypes.c_int)]
    x = ctypes.c_int

class P(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int), ('x', ctypes.c_int)]
    x = ctypes.c_int

