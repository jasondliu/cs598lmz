import ctypes
# Test ctypes.CFUNCTYPE
cfunc_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_long)
def cfunc(name, name_len, offset):
    return 0xFFFF
def f():
    return cfunc_type(cfunc)
f()
