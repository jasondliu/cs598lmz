import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int),
                ('x', ctypes.c_int),
                ('x', ctypes.c_int)]

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('x', ctypes.c_int),
                ('x', ctypes.c_int)]

S2()
S()
