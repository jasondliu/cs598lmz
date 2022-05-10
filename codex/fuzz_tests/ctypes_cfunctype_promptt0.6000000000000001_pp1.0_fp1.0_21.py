import ctypes
# Test ctypes.CFUNCTYPE and ctypes.POINTER with a function returning a pointer.
# This will fail on windows because of missing 'const' keyword.
#
# The problem is that the 'const' keyword is not part of the function
# declaration, but the function definition.

from ctypes import *
from ctypes.test import is_resource_enabled

if not is_resource_enabled("printing"):
    print("Skipped")
    raise SystemExit

if sys.platform == "win32":
    import _ctypes_test
    dll = CDLL(_ctypes_test.__file__)
    # dll = CDLL("ctypes_test.dll")
else:
    dll = CDLL(None)

func = CFUNCTYPE(POINTER(c_int))(("testfunc_si_p", dll))
func.restype = POINTER(c_int)

ptr = func()
print(ptr[0])
ptr[0] = 42
print(ptr[0])

# The same test with a different restype:
#
# func.restype
