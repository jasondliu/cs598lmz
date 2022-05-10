import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

# The following example uses the C library function qsort() to sort the
# integers of a list, in ascending numerical order.

qsort = ctypes.CDLL(None).qsort
qsort.argtypes = (ctypes.c_void_p, # void *base
                  ctypes.c_size_t, # size_t num
                  ctypes.c_size_t, # size_t size
                  FUNTYPE)        # int (*compar)(const void *, const void *)

def py_cmp_func(a, b):
    print("a: %d, b: %d" % (a, b))
    return ctypes.c_int(a-b).value
cmp_func = FUNTYPE(py_cmp_func)

# Now the following call sorts the array:

array = (ctypes.c_int * 5)(5, 4, 3, 2, 1)
n = len(array)
qsort(array, n, ctypes.sizeof(
