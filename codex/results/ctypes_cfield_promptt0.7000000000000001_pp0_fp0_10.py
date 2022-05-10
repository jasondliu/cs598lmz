import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

# Test ctypes.Field
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_long),
                ("c", ctypes.c_double),
                ('d', ctypes.c_char),
                ('e', ctypes.c_char_p),
                ('f', ctypes.c_byte),
                ('g', ctypes.c_ubyte),
                ('h', ctypes.c_short),
                ('i', ctypes.c_ushort),
                ('j', ctypes.c_uint),
                ('k', ctypes.c_longlong),
                ('l', ctypes.c_ulonglong),
                ('m', ctypes.c_float),
                ('n', ctypes.c_void_p)]

# Test ctypes.Array
class Z(ctypes.Structure):
    _fields_ = [("a",
