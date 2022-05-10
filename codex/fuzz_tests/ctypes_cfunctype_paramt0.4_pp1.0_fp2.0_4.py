import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def func(a, b):
    return a + b

f = FUNTYPE(func)
f(1, 2)

# ctypes.c_int * 4
# ctypes.c_int * 4
# ctypes.POINTER(ctypes.c_int)

# ctypes.c_int * 4
# ctypes.c_int * 4
# ctypes.POINTER(ctypes.c_int)

# ctypes.c_int * 4
# ctypes.c_int * 4
# ctypes.POINTER(ctypes.c_int)

# ctypes.c_int * 4
# ctypes.c_int * 4
# ctypes.POINTER(ctypes.c_int)

# ctypes.c_int * 4
# ctypes.c_int * 4
# ctypes.POINTER(ctypes.c_int)

# ctypes.c_int * 4
# ctypes.c_int * 4
# c
