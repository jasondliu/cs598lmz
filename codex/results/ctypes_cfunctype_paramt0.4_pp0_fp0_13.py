import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(n):
    return n * 10

cfunc = FUNTYPE(myfunc)
print cfunc(5)

# ctypes.wintypes.LP_c_long
# ctypes.wintypes.LP_c_ulong
# ctypes.wintypes.LP_c_void_p
# ctypes.wintypes.LP_c_char_p
# ctypes.wintypes.LP_c_wchar_p
# ctypes.wintypes.LP_c_byte
# ctypes.wintypes.LP_c_ubyte
# ctypes.wintypes.LP_c_short
# ctypes.wintypes.LP_c_ushort
# ctypes.wintypes.LP_c_int
# ctypes.wintypes.LP_c_uint
# ctypes.wintypes.LP_c_longlong
# ctypes.wintypes.LP_c_ulonglong
# ctypes.wintypes.LP_c
