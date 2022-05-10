import ctypes
# Test ctypes.CFUNCTYPE

def func(*args):
    return args

test_types = [
    ctypes.c_bool,
    ctypes.c_byte,
    ctypes.c_char,
    ctypes.c_wchar,
    ctypes.c_ubyte,
    ctypes.c_short,
    ctypes.c_ushort,
    ctypes.c_int,
    ctypes.c_uint,
    ctypes.c_long,
    ctypes.c_ulong,
    ctypes.c_longlong,
    ctypes.c_ulonglong,
    ctypes.c_float,
    ctypes.c_double,
    ctypes.c_longdouble,
    ctypes.c_char_p,
    ctypes.c_wchar_p,
    ctypes.c_void_p,
]

def test_func(type):
    return ctypes.CFUNCTYPE(type, type)(func)

def test_func_byval(type):
    return ctypes.CFUNCT
