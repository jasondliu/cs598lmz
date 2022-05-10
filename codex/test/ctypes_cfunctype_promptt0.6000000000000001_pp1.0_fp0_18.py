import ctypes
# Test ctypes.CFUNCTYPE with different argument types.
def f(x):
    return x

ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(f)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char)(f)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_short)(f)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_long)(f)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_longlong)(f)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float)(f)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)(f)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(f)
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(f)
