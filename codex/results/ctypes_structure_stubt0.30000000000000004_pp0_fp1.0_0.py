import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

s2 = S(1, 2, 3)
print(s2.x, s2.y, s2.z)

# ctypes.Structure
# ctypes.Union
# ctypes.Array
# ctypes.c_char
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
# ctypes.c_w
