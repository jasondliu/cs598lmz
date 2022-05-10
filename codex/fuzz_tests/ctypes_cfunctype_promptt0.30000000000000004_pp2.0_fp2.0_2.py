import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

#
# The following functions are defined in _ctypes_test.c:
#
# int func(int)
# int func_caller(int (*func)(int), int arg)
# int func_caller_i(int (*func)(int), int arg)
# int func_caller_ii(int (*func)(int), int arg)
# int func_caller_iii(int (*func)(int), int arg)
# int func_caller_iiii(int (*func)(int), int arg)
# int func_caller_iiiii(int (*func)(int), int arg)
# int func_caller_iiiiii(int (*func)(int), int arg)
# int func_caller_iiiiiii(int (*func)(int), int arg)
# int func_caller_iiiiiiii(int (*func)(int), int arg)
# int func_caller_iiiiiiiii(int (*func)(int), int arg)
# int
