import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is only meant to be run in a Python process that has been
# started with the -S option.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is declared in _ctypes_test.c as:
#   int printf(const char *format, ...);
printf = lib.printf
printf.argtypes = ctypes.c_char_p,
printf.restype = ctypes.c_int

# This function is declared in _ctypes_test.c as:
#   int printf2(const char *format, ...);
printf2 = lib.printf2
printf2.argtypes = ctypes.c_char_p,
printf2.restype = ctypes.c_int

# This function is declared in _ctypes_test.c as:
#   int printf3(const char *format, ...);
printf3 = lib.printf3
printf3.argtypes = ctypes.c_char_p,
printf3.restype = ctypes.c_int

