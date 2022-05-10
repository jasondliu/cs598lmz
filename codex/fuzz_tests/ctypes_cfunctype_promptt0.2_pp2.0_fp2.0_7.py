import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have a simple prototype, taking
# an integer and returning an integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_cmp_func(i):
    print("py_cmp_func", i)
    return -i

cmp_func = CMPFUNC(py_cmp_func)

# Call the function in the dll.

lib.pass_func(cmp_func)

# The function pointer is passed to qsort(), which should call
# our function to compare two integers.

array = (ctypes.c_int * 5)(5, 4, 3, 2, 1)
lib.qsort.restype = None
lib.qsort(array, len(array), ctypes.sizeof(ctypes.c_int), cmp_func)

for i in array
