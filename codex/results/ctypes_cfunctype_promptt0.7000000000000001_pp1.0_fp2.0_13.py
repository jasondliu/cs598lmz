import ctypes
# Test ctypes.CFUNCTYPE

# It turns out that CFUNCTYPE doesn't always use a PyCFunction,
# but can use a CFUNCTYPE-based function instead, in which case
# the type of the arguments must be specified explicitly.

import _ctypes_test

if not hasattr(_ctypes_test, 'set_callback'):
    raise ImportError("requires _ctypes_test module from Python test suite")

# This test is for both CFUNCTYPE and the 'restype' and 'argtypes'
# attributes of the returned instance.

FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

callback = FUNC(lambda x: x * 10)
_ctypes_test.set_callback(callback)

assert _ctypes_test.callback_in_dll(1) == 10
assert _ctypes_test.callback_in_dll(2) == 20
assert _ctypes_test.callback_in_dll(3) == 30
