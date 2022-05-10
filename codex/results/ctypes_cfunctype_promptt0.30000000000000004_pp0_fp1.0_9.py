import ctypes
# Test ctypes.CFUNCTYPE

# This test is for the case where the function type is declared
# before the function.

libc = ctypes.CDLL(ctypes.util.find_library('c'))

# XXX: This is a hack, but I don't know how to do it better
# The problem is that the function type is not known at the time
# the function is declared.
# This is not a problem with the real C compiler, because the
# function type is declared before the function.

# The function type is declared here:
c_printf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

# This is the function declaration:
libc.printf = c_printf(("printf", libc))

# This is the function call:
libc.printf("Hello, World\n")
