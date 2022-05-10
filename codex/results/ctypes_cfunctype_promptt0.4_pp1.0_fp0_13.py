import ctypes
# Test ctypes.CFUNCTYPE.

from ctypes import *

if sizeof(c_int) != sizeof(c_void_p):
    # 64-bit
    c_ptrdiff_t = c_int64
    c_size_t = c_uint64
else:
    c_ptrdiff_t = c_int
    c_size_t = c_uint

# XXX This is a workaround for a bug in Mingw32, where c_void_p is
# defined as c_ulong instead of c_void_p.
if sizeof(c_void_p) == sizeof(c_ulong):
    c_void_p = c_ulong

# XXX This is a workaround for a bug in Mingw32, where c_longlong is
# defined as c_long instead of c_longlong.
if sizeof(c_longlong) == sizeof(c_long):
    c_longlong = c_long

# XXX This is a workaround for a bug in Mingw32, where c_ulonglong is
# defined as c_ulong instead of c_ulonglong.
