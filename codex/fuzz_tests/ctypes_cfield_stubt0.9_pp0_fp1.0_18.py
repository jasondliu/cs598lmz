import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x) # type: ignore

if sizeof(ctypes.c_long) == 4:
    ctypes.c_longlong = ctypes.c_long
    ctypes.c_ulonglong = ctypes.c_ulong
else:
    ctypes.c_longlong = ctypes.c_longlong
    ctypes.c_ulonglong = ctypes.c_ulonglong

c_float = ctypes.c_float
c_double = ctypes.c_double

c_longdouble = ctypes.c_longlong # type: ignore

c_long = ctypes.c_long
c_ulong = ctypes.c_ulong
c_longlong = ctypes.c_longlong
c_ulonglong = ctypes.c_ulonglong

class Namespace(dekit.Namespace):
    _rawtypes = dict(c_byte='char',
                     c_ubyte='unsigned char',
                     c_short='short',
                     c_int='int',
                     c_uint='unsigned int',
                     c_long='
