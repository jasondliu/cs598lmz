import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('b', ctypes.c_byte),
                ('h', ctypes.c_short),
                ('i', ctypes.c_int),
                ('l', ctypes.c_long),
                ('f', ctypes.c_float),
                ('d', ctypes.c_double),
                ('c', ctypes.c_char),
                ('s', ctypes.c_char_p),
                ('u', ctypes.c_wchar_p),
                ('p', ctypes.c_void_p),
                ('o', ctypes.py_object),
                ('t', ctypes.c_char * 4),
                ('T', ctypes.c_wchar * 4),
                ('a', ctypes.c_int * 4),
                ('b1', ctypes.c_byte * 4),
                ('h1', ctypes.c_short * 4),
                ('i1', ctypes.c_int * 4),
                ('l1', ctypes.c_long
