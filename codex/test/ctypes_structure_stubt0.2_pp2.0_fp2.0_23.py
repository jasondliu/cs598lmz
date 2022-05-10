import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.c_int
# ctypes.c_char
# ctypes.c_char_p
# ctypes.c_void_p
# ctypes.c_float
# ctypes.c_double
# ctypes.c_bool
# ctypes.c_short
# ctypes.c_long
# ctypes.c_longlong
# ctypes.c_ubyte
# ctypes.c_ushort
# ctypes.c_ulong
# ctypes.c_ulonglong
# ctypes.c_ssize_t
# ctypes.c_size_t
# ctypes.c_wchar
# ctypes.c_wchar_p
# ctypes.c_void_p
# ctypes.c_char_p
# ctypes.c_wchar_p
# ctypes.c_void_p
# c
