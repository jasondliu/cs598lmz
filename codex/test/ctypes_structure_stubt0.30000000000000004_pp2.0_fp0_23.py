import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 10
s.y = 20

print(s.x, s.y)

# ctypes.Structure.from_address()
# ctypes.Structure.from_buffer()
# ctypes.Structure.from_buffer_copy()

# ctypes.Union

# ctypes.c_bool
# ctypes.c_byte
# ctypes.c_char
# ctypes.c_char_p
# ctypes.c_double
# ctypes.c_float
# ctypes.c_int
# ctypes.c_long
# ctypes.c_longdouble
# ctypes.c_longlong
# ctypes.c_short
# ctypes.c_ubyte
# ctypes.c_uint
# ctypes.c_ulong
# ctypes.c_ulonglong
# ctypes.c_ushort
# ctypes.c_void_p
# ctypes.c_wchar
# ctypes.
