import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument, and return
# an integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be called.

@CMPFUNC
def func(i):
    print('func', i)
    return i

# Call the function in the dll.  The integer it returns is the
# address of the function pointer it got as argument.

addr = lib.pass_in_out(func)
print('addr', addr)

# Now call the function via the function pointer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

func = CMPFUNC(addr)
print('func', func)
print(func(42))

# This is a function that takes
