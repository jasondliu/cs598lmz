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

array = (ctypes.c_int * 5)()
for i in range(5):
    array[i] = i

lib.my_qsort(array, len(array), ctypes.sizeof(ctypes.c_int), cmp_func)

for i in range(5):
    assert array[i] == i

# test passing None as callback
try:
    lib.my_qsort(array, len(array), ctypes.sizeof(ctypes.c_int), None)
except TypeError
