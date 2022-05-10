import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

class Z(X):
    _fields_ = [('b', ctypes.c_byte),
                ('c', ctypes.c_byte),
                ('d', ctypes.c_byte),
                ('e', ctypes.c_byte),
                ('f', ctypes.c_byte),
                ('g', ctypes.c_byte),
                ('h', ctypes.c_byte),
                ('i', ctypes.c_byte),
                ('j', ctypes.c_byte),
                ('k', ctypes.c_int),
                ('l', ctypes.c_int),
                ('m', ctypes.c_int),
                ('n', ctypes
