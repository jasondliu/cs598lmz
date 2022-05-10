import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int, 2),
                ('b', ctypes.c_int, 1),
                ('c', ctypes.c_int, 2),
                ('d', ctypes.c_int, 3)]

class Y(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int, 2),
                ('b', ctypes.c_int, 1),
                ('c', ctypes.c_int, 2),
                ('d', ctypes.c_int, 3),
                ('e', ctypes.c_int, 3)]

class Z(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int, 2),
                ('b', ctypes.c_int, 1),
                ('c', ctypes.c_int, 2),
                ('d', ctypes.c_int, 3),
                ('e', ctypes.c_int, 3),
                ('f', ctypes.c_int
