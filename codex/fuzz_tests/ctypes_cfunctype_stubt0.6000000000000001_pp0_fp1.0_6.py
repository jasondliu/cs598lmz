import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()

#ctypes.c_char_p
#ctypes.c_void_p

#ctypes.c_long
#ctypes.c_ulong

#ctypes.c_longlong
#ctypes.c_ulonglong

#ctypes.c_double
#ctypes.c_float

#ctypes.c_int
#ctypes.c_uint

#ctypes.c_short
#ctypes.c_ushort

#ctypes.c_byte
#ctypes.c_ubyte

#ctypes.c_bool

#ctypes.c_char
#ctypes.c_wchar
