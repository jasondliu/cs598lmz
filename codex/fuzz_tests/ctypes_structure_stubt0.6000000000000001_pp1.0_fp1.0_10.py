import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)
    y = ctypes.c_double(2.0)
    z = ctypes.c_double(3.0)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double),
                ('z', ctypes.c_double)]

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_double),
                ('y', ctypes.c_double),
                ('z', ct
