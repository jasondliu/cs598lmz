import ctypes
# Test ctypes.CField with sizes of 4 and 8 (for 32- and
# 64-bit platforms).
INT_SIZE = ctypes.sizeof(ctypes.c_int)
FLOAT_SIZE = ctypes.sizeof(ctypes.c_float)
if INT_SIZE == 4 and FLOAT_SIZE == 4:
    class Point3D(ctypes.Structure):
        _fields_ = [('x', ctypes.c_float),
                    ('y', ctypes.c_float),
                    ('z', ctypes.c_float)]
elif INT_SIZE == 4 and FLOAT_SIZE == 8:
    class Point3D(ctypes.Structure):
        _fields_ = [('x', ctypes.c_double),
                    ('y', ctypes.c_double),
                    ('z', ctypes.c_double)]
else:
    raise ValueError('Unknown size: int = %d, float = %d' %
                     (INT_SIZE, FLOAT_SIZE))
