import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

ctypes.CField = type(S2.x)

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int)]

ctypes.CField = type(S3.x)

class S4(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int), ('w', ctypes.c_int)]

ctypes.CField = type(S4.x)

class S5(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int), ('w', ctypes.c_int), ('v', c
