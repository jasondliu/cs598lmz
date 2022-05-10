import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class B(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', S)]

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', S),
                ('d', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', S),
                ('d', ctypes.c_int),
                ('e', ctypes.c_int)]

