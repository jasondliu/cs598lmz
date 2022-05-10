import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    _fields_ = [('x', ctypes.c_int, 2)]

def f():
    ctypes.c_int(1)
    ctypes.c_int(1, 2)
    ctypes.c_int(1, 2, 3)
    ctypes.c_int(1, 2, 3, 4)
    ctypes.c_int(1, 2, 3, 4, 5)
    ctypes.c_int(1, 2, 3, 4, 5, 6)
    ctypes.c_int(1, 2, 3, 4, 5, 6, 7)
    ctypes.c_int(1, 2, 3, 4, 5, 6, 7, 8)
    ctypes.c_int(1, 2, 3, 4, 5, 6, 7, 8, 9)
    ctypes.c_int(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
