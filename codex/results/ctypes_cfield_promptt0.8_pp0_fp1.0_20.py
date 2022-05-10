import ctypes
# Test ctypes.CField

import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

assert X.a.offset == 0
assert X.a.size == ctypes.sizeof(ctypes.c_int)

assert ctypes.offsetof(X, "a") == 0
assert ctypes.sizeof(X) == ctypes.sizeof(ctypes.c_int)

# ctypes should support field names with '_'
# https://github.com/python/cpython/pull/211

class X(ctypes.Structure):
    _fields_ = [("a_b", ctypes.c_int)]

assert X.a_b.offset == 0
assert X.a_b.size == ctypes.sizeof(ctypes.c_int)

assert ctypes.offsetof(X, "a_b") == 0

# ctypes should support field names with '__'
# https://github.com/python/cpython/pull/212

class X(ctypes.Structure):
