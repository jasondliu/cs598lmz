import ctypes
# Test ctypes.CFUNCTYPE with no args

from ctypes import *
import _ctypes_test

libc = CDLL(_ctypes_test.__file__)

# First create a prototype
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

# Next, an array type
# cmp_func is a user data item in the call back function
# we have to pass a pointer to the function, not just the function
CMPARRTYPE = c_int * 2
cmp_func = CMPFUNC(libc.callbacks[0])

# Now, the final function
qsort = libc.my_qsort
qsort.restype = None
qsort.argtypes = [POINTER(c_void_p), c_int, c_int, CMPARRTYPE]

a = [-45, -4, -2, 1, 3, 10, 23, 45, 123, 200, 456]

print 'Before:', a
qsort(a, len(a), sizeof(c_int), [addressof(cmp_func), 0
