import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_float),
                ('c', ctypes.c_char),
                ('d', ctypes.c_byte),
                ('e', ctypes.c_short),
                ('f', ctypes.c_long),
                ('g', ctypes.c_double),
                ('h', ctypes.c_longlong),
                ('i', ctypes.c_void_p),
                ('j', ctypes.c_char_p),
                ('k', ctypes.c_wchar_p),
                ('l', ctypes.c_int * 2),
                ('m', ctypes.c_char_p * 2),
                ('n', ctypes.c_int * 2 * 2),
                ('o', ctypes.c_char_p * 2 * 2),
                ('p', ctypes.c_void_p * 2),
                ('q', ctypes.c_char_p * 2 * 2 * 2
