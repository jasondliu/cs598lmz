import ctypes
# Test ctypes.CFUNCTYPE without param flags (where possible)

from ctypes import *

def test(tp):
    proto = CFUNCTYPE(tp)
    v = proto(lambda x: x)
    res = v(42)
    print(tp, v, res)
    assert res == 42

test(c_int)
test(c_char_p)
test(POINTER(c_int))

if sizeof(c_long) == sizeof(c_void_p):
    test(c_long)
    test(c_ulong)
    test(c_void_p)
    test(py_object)
else:
    test(c_longlong)
    test(c_ulonglong)

try:
    test(c_ssize_t)
except ValueError:
    import _ctypes_test
    _ctypes_test.slong_type == c_longlong
    test(c_longlong)

test(c_ulong)
test(c_long)
