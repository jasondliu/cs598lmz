import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is declared as:
# int printf(const char *format, ...);
# so we must set the argtypes.
lib.printf.argtypes = ctypes.c_char_p,

# Call printf
lib.printf(b"Hello, %s!\n", b"world")

# Now we can create a CFUNCTYPE object, and use it to call printf
# directly.
PRINTF = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(("printf", lib))
PRINTF(b"Hello, %s!\n", b"world")

# The CFUNCTYPE object can be used as a function attribute
# of a ctypes.CDLL instance.
lib.my_printf = PRINTF
lib.my_printf(b"Hello, %s!\n", b"world")

# The CFUNCTYPE object can be used as a function attribute

