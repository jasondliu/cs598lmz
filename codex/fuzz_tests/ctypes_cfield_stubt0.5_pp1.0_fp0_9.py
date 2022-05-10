import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int)]

class S4(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int),
                ('z', ctypes.c_int), ('t', ctypes.c_int)]

class S5(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int),
                ('z', ctypes.c_int), ('t', ctypes.c_int),
                ('u', ctypes.c_int)]

class S6(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', c
