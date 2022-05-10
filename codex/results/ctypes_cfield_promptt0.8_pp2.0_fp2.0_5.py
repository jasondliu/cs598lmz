import ctypes
# Test ctypes.CField
class XX(ctypes.Structure):
    _fields_ = [
        ("c_int_field", ctypes.c_int),
        ("c_void_p_field", ctypes.c_void_p),
    ]

ctypes.c_int(1).value
c = ctypes.c_int(1)
c.value = 2

ctypes.c_byte(2).value
ctypes.c_ubyte(2).value
ctypes.c_short(2).value
ctypes.c_ushort(2).value
ctypes.c_int(2).value
ctypes.c_uint(2).value
ctypes.c_long(2).value
ctypes.c_ulong(2).value
ctypes.c_longlong(2).value
ctypes.c_ulonglong(2).value
ctypes.c_float(2).value
ctypes.c_double(2).value
ctypes.c_longdouble(2).value
ctypes.c_char("a").value
ctypes.c_w
