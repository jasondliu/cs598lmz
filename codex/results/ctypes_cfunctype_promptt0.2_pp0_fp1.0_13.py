import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is declared in _ctypes_test.h:
#
#    int printf(const char *format, ...);
#
# and the argtypes list is set to (c_char_p, ...)
#
# The ellipsis in the declaration is mapped to a tuple argument
# in the argtypes list.
#
# The function is called with a format string and two arguments,
# the result is the length of the formatted string:

printf = lib.printf
printf.argtypes = (ctypes.c_char_p, ctypes.c_int, ctypes.c_double)
printf.restype = ctypes.c_int

result = printf("%d %f\n", 42, 3.14)
if result == -1:
    raise OSError("printf returned -1")
print("result", result)

# The following call should fail with a TypeError:
try:
    result = printf("%d %f\n
