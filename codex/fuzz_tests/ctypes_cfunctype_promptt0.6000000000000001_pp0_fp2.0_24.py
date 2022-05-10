import ctypes
# Test ctypes.CFUNCTYPE (issue #13390).
def test_CFUNCTYPE():
    import _ctypes
    API = [('f', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))]
    dll = ctypes.CDLL(_ctypes.__file__)
    try:
        dll.f.argtypes = (ctypes.c_int,)
        dll.f.restype = ctypes.c_int
    except AttributeError:
        pass
    else:
        raise Exception


def test_wintypes():
    from ctypes.wintypes import (
        c_int, c_uint, c_short, c_ushort, c_long, c_ulong, c_longlong,
        c_ulonglong, c_double, c_wchar, c_char, c_byte, c_ubyte, c_char_p,
        c_wchar_p, c_void_p, c_bool, c_size_t, c_ssize_t, c_int8,
