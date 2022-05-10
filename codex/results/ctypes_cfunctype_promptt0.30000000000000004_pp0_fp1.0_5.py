import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# The CFUNCTYPE() factory creates a type suitable for use with
# the restype and argtypes attributes of the C function.
#
# The prototype of the function is:
#   char *my_strchr(char *s, char c)

my_strchr = lib.my_strchr
my_strchr.restype = ctypes.c_char_p
my_strchr.argtypes = (ctypes.c_char_p, ctypes.c_char)

# The prototype of the function is:
#   char *my_strchr2(char *s, char c)

my_strchr2 = lib.my_strchr2
my_strchr2.restype = ctypes.c_char_p
my_strchr2.argtypes = (ctypes.c_char_p, ctypes.c_char)

# The prototype of the function is:
#   char
