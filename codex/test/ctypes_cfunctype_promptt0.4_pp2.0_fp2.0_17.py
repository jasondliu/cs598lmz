import ctypes
# Test ctypes.CFUNCTYPE()
#
# The first argument to CFUNCTYPE() is the return type.  The rest are
# the argument types.  The arguments are in order, so if the function
# takes an argument "x" then "int" must be the second argument to
# CFUNCTYPE().
#
# The function is called by passing a tuple of arguments.  So if the
# function takes arguments "x" and "y", then to call it you pass
# (x,y) as the argument to the function.
#
# The function returns the result of the call, so to assign to the
# result of the function you just write "result = func(args)".
#
# Example: to call
#   int printf(const char *format, ...);
# you would use:
#   printf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(("printf", libc))
#
# To call printf you would then use:
#   printf(("%d %d\n", (ctypes.c_int(1), ctypes.c
