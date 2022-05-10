import ctypes
# Test ctypes.CFUNCTYPE with an empty argtype list.
import _ctypes
#
# This tests the case where the function takes no arguments.
#
def func():
    return 42

try:
    FUNC_TYPE = ctypes.CFUNCTYPE(ctypes.c_int)
except TypeError:
    raise SystemExit

f = FUNC_TYPE(func)
assert f() == 42
