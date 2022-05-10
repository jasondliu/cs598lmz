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
    return i * 2

# Call the function in the dll.  The integer it returns is the
# address of the function pointer it was passed.

addr = lib.pass_in_function(func)
print('addr', addr)

# Now call the function via the function pointer.

lib.call_through_funcptr(addr, 12)

# Now call the function via the function pointer, but with an
# incorrect argument type.  This should raise a TypeError.

try:
    lib.call_through_funcptr(addr, 'hello
