import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# This is the prototype of the callback function
# int __stdcall callback(int a, int b)
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def mycmp(a, b):
    print "mycmp", a, b
    return a - b

# This is the prototype of the function taking the callback
# int __stdcall qsort(void *base, size_t nelem, size_t width, int (__stdcall *fcmp)(const void *, const void *));
qsort = ctypes.cdll.msvcrt.qsort
qsort.argtypes = (ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, CMPFUNC)
qsort.restype = ctypes.c_int

# This is the prototype of the function taking the callback
# int __stdcall bsearch(const void *key, const void *base, size_t nelem, size
