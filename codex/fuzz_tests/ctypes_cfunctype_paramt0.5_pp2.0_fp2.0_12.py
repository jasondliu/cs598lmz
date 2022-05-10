import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def py_func(x):
    return x + 1

c_func = FUNTYPE(py_func)

print(c_func(2))

# ctypes.c_char
# ctypes.c_wchar
# ctypes.c_byte
# ctypes.c_ubyte
# ctypes.c_short
# ctypes.c_ushort
# ctypes.c_int
# ctypes.c_uint
# ctypes.c_long
# ctypes.c_ulong
# ctypes.c_longlong
# ctypes.c_ulonglong
# ctypes.c_float
# ctypes.c_double
# ctypes.c_longdouble
# ctypes.c_char_p
# ctypes.c_wchar_p
# ctypes.c_void_p

# ctypes.c_bool
# ctypes.c_char
# ctypes.c_wchar
# ctypes.c_byte
# ctypes.c_uby
