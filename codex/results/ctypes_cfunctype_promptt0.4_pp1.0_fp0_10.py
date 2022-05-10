import ctypes
# Test ctypes.CFUNCTYPE.
# This tests the case where the function has no arguments.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

prototype = ctypes.CFUNCTYPE(ctypes.c_int)
restype = ctypes.c_int

f = prototype((b"_ctypes_testfunc_v", lib))
assert f() == 42

f = prototype((b"_ctypes_testfunc_v", lib), None)
assert f() == 42

f = prototype((b"_ctypes_testfunc_v", lib), restype)
assert f() == 42

f = prototype((b"_ctypes_testfunc_v", lib), restype, None)
assert f() == 42

f = prototype((b"_ctypes_testfunc_v", lib), None, None)
assert f() == 42

f = prototype((b"_ctypes_testfunc_v", lib), restype, ())
assert f() == 42

f = prototype((b"_ctypes_testfunc_v
