import io
# Test io.RawIOBase
try:
    io.RawIOBase
except AttributeError:
    # Python < 3.2
    class RawIOBase(object):
        pass
    io.RawIOBase = RawIOBase

from ctypes import (
    POINTER, Structure, Union, c_bool, c_byte, c_char, c_char_p, c_double,
    c_float, c_int, c_int16, c_int32, c_int64, c_int8, c_long, c_longlong,
    c_short, c_ubyte, c_uint, c_uint16, c_uint32, c_uint64, c_uint8, c_ulong,
    c_ulonglong, c_ushort, c_void_p, c_wchar, c_wchar_p,
    CFUNCTYPE, POINTER, Structure, Union, pointer, sizeof,
    addressof, alignment, byref, cast, create_string_buffer,
    get_errno, get_last_error, memmove, memset, resize,
