import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is the prototype of the function we want to call:
# int printf(const char *format, ...);

# The argtypes and restype attributes tell ctypes what the function
# prototype looks like.

lib.my_printf.argtypes = ctypes.c_char_p,
lib.my_printf.restype = ctypes.c_int

# Now we can call the function.

lib.my_printf("Hello, %s!\n", "World")

# The prototype of the function we want to call is:
# int add(int a, int b);

lib.my_add.argtypes = ctypes.c_int, ctypes.c_int
lib.my_add.restype = ctypes.c_int

print(lib.my_add(1, 2))

# The prototype of the function we want to call is:
# int add_floats(float a, float b);

lib.my_add
