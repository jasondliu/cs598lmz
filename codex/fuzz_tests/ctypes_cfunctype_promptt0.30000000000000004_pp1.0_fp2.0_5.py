import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is declared in _ctypes_test.c as:
#
#   int func(int(*)(int))
#
# So the first argument is a pointer to a function taking an int
# argument and returning an int.

# This function is declared in _ctypes_test.c as:
#
#   int func2(int(*)(int, int))
#
# So the first argument is a pointer to a function taking two int
# arguments and returning an int.

# This function is declared in _ctypes_test.c as:
#
#   int func3(int(*)(int, int, int))
#
# So the first argument is a pointer to a function taking three int
# arguments and returning an int.

# This function is declared in _ctypes_test.c as:
#
#   int func4(int(*)(int, int, int, int))
#
# So the first argument is a pointer to a function taking four int

