import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(object):
    _fields_ = [('s', S)]

class C1(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class C2(C1):
    _fields_ = [('c', ctypes.c_int),
                ('d', ctypes.c_int)]

class C3(C2):
    _fields_ = [('e', ctypes.c_int),
                ('f', ctypes.c_int)]

class C4(C3):
    _fields_ = [('g', ctypes.c_int),
                ('h', ctypes.c_int)]

class D1(ctypes.Union):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class D2(D1):
    _fields_ = [('c', ctypes.c_int),
                ('d', ctypes.c
