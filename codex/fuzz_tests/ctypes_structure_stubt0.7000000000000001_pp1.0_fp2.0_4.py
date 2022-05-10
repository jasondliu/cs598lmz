import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int * 4)]

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 4)]
    x = ctypes.c_int

class U(ctypes.Structure):
    _anonymous_ = ('s',)
    _fields_ = [('s', S), ('y', ctypes.c_int)]

class V(ctypes.Structure):
    _anonymous_ = ('s',)
    _fields_ = [('y', ctypes.c_int), ('s', S)]

class W(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    _anonymous_ = ('s',)
    _fields_ = [('s', S)]

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 4)]
    _anonymous_ = ('x',)
