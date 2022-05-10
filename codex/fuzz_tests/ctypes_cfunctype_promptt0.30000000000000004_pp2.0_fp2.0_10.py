import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# This test is not really complete, but it's a start.
#

#
# First, a function that takes a function pointer as argument
#

# The function prototype is:
# int callit(int(*func)(int))

CALLITPROTO = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The function to be passed to callit():

def func(val):
    print("func() called with", val)
    return val + 1

# Convert the Python function into a function pointer.
CMPFUNC = CALLITPROTO(func)

# Now call callit():

r = lib.callit(CMPFUNC)
print("callit() returned", r)

#
# Now a function that returns a function pointer
#

# The function prototype is:
# int(*getit())(int)

GETITPROTO = ctypes.CFUNCT
