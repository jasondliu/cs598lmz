import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int)]

class Y(X):
    _fields_ = [('e', ctypes.c_int),
                ('f', ctypes.c_int),
                ('g', ctypes.c_int),
                ('h', ctypes.c_int)]

class Z(Y):
    _fields_ = [('i', ctypes.c_int),
                ('j', ctypes.c_int),
                ('k', ctypes.c_int),
                ('l', ctypes.c_int)]

class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int)]

class B(ctypes
