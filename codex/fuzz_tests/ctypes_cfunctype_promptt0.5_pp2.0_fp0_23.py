import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# define a callback function
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_cmp_func(a, b):
    print 'py_cmp_func(%d, %d)' % (a, b)
    return a - b

cmp_func = CMPFUNC(py_cmp_func)

# call a C function with a callback
lib.set_qsort_callback(cmp_func)

# call the C qsort function, which uses the callback
a = (ctypes.c_int * 5)(5, 4, 3, 2, 1)
lib.my_qsort(5, a)

lib.set_qsort_callback(None)

# call the C qsort function, which now uses the default callback
a = (ctypes.c_int * 5)(5, 4, 3, 2, 1)
lib
