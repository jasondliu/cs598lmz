import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(x, y, z):
    return x + y + z

f.restype = ctypes.c_int
f.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]

f(1, 2, 3)

f.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]

f(1, 2, 3)

f.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]

f(1, 2, 3)

f.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]

f(1, 2, 3)

f.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]

f(1, 2, 3)

f
