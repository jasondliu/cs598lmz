import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

lib.test(1, 2, 3, S(1, 2, 3,))
</code>

