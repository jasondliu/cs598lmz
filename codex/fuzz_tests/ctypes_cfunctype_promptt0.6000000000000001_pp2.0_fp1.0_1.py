import ctypes
# Test ctypes.CFUNCTYPE for calling C functions with variadic arguments

import _ctypes_test

libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Call printf

PRINTF_FORMAT = ctypes.c_char_p
printf = ctypes.CFUNCTYPE(ctypes.c_int, PRINTF_FORMAT, *([ctypes.c_int] * 5))(("printf", libc))

# XXX: These tests fail with python-gcc on Linux/x86_64,
#      but use the system printf instead.
#
#      The reason seems to be that python-gcc uses
#      the python interpreter's printf, which is
#      different from the one used by the interpreter.

#print printf("Hello")
#print printf("Hello %s", "World")
#print printf("%s %s %s %s %s", "a", "b", "c", "d", "e")

# Call sprintf

SPRINTF_FORMAT = ctypes.c_char_p
sprintf =
