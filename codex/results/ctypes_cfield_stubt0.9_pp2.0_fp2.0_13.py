import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(ctypes.Structure):
    _fields_ = [('a', ctypes.c_byte),
                ('b', ctypes.c_ubyte),
                ('c', ctypes.c_short),
                ('d', ctypes.c_ushort),
                ('e', ctypes.c_int),
                ('f', ctypes.c_uint),
                ('g', ctypes.c_long),
                ('h', ctypes.c_ulong),
                ('i', ctypes.c_longlong),
                ('j', ctypes.c_ulonglong),
                ('k', ctypes.c_float),
                ('l', ctypes.c_double),
                ('m', ctypes.c_char_p),
                ('n', ctypes.c_char*3),
                ('o', ctypes.c_char*3),
                ('q', ctypes.c_byte),
                ('r', ctypes.c_wchar_p),
                ('s', ctypes.c_wchar*3),
                ('t
