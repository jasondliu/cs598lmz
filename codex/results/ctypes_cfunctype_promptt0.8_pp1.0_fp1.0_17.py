import ctypes
# Test ctypes.CFUNCTYPE function generation
#
# The original test would cause a segmentation fault when called, but
# appears to be working now.  Changed to a different test.
#
# written by Thomas Heller

import _ctypes_test

NULL = None

f = _ctypes_test.get_callback()

assert f.argtypes == [_ctypes_test.LP_c_int]
assert f.restype == ctypes.c_int

x = ctypes.c_int(42)
r = f(ctypes.pointer(x))
assert r == 42

assert x.value == 42
