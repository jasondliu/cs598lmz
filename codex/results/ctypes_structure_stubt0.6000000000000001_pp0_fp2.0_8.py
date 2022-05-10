import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int, 1)]

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int, 1)]
    x = ctypes.c_int

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int, 1)]
    x = ctypes.c_int * 2

class S4(ctypes.Structure):
    x = ctypes.c_int * 2
    _fields_ = [('x', ctypes.c_int, 1)]

# the following will fail:
# class S5(ctypes.Structure):
#     _fields_ = [('x', ctypes.c_int, 1)]
#     x = ctypes.c_int * 3

# class S6(ctypes.Structure):
#     x = ctypes.c_int * 3
#     _fields_ = [('x', ctypes.c_int, 1)]

# class
