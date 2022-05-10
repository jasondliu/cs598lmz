import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    return a + b

myfunc_c = FUNTYPE(myfunc)

print(myfunc_c(1, 2))

# ctypes.c_int32
# ctypes.c_int64
# ctypes.c_int16
# ctypes.c_int8
# ctypes.c_uint32
# ctypes.c_uint64
# ctypes.c_uint16
# ctypes.c_uint8
# ctypes.c_float
# ctypes.c_double
# ctypes.c_bool

# ctypes.c_char_p
# ctypes.c_wchar_p
# ctypes.c_void_p
# ctypes.c_char
# ctypes.c_wchar

# ctypes.c_byte
# ctypes.c_ubyte
# ctypes.c_short
# ctypes.c_ushort
# ctypes.c_int
#
