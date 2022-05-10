import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x+1

f = FUNTYPE(func)
f(2)

# ctypes.c_int32
# ctypes.c_uint32
# ctypes.c_int64
# ctypes.c_uint64
# ctypes.c_float
# ctypes.c_double
# ctypes.c_char_p
# ctypes.c_void_p
# ctypes.c_wchar_p

# ctypes.POINTER(ctypes.c_int)
# ctypes.POINTER(ctypes.c_double)

# ctypes.c_int * 2
# ctypes.c_int * 3
# ctypes.c_double * 2
# ctypes.c_double * 3

# ctypes.c_int * 3 * 2
# ctypes.c_double * 3 * 2

# ctypes.c_int * 3 * 2 * 2
# ctypes.c_double * 3 * 2 * 2

# c
