import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)
#
# This is a test of a function that takes a function pointer as an argument.
#
# This test is derived from a test written by Thomas Heller.

if os.name == "nt":
    stdcall = ctypes.WINFUNCTYPE
else:
    stdcall = ctypes.CFUNCTYPE

import _ctypes_test
dll = ctypes.CDLL(_ctypes_test.__file__)

# the function prototype is:
# int (__stdcall *func)(int)
func = stdcall(ctypes.c_int, ctypes.c_int)

# the function to be passed as argument:
def myfunc(val):
    return val + 1

# the function to be called with the function pointer:
funcptr = dll._testfunc_p_p
funcptr.argtypes = (func,)
funcptr.restype = ctypes.c_int

# the function to be called with the function pointer:
funcptr2 = dll._testfunc_p_p
funcptr2.arg
