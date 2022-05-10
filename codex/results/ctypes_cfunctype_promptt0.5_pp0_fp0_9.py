import ctypes
# Test ctypes.CFUNCTYPE
def func(x, f):
    return f(x)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def py_cmp(x, y):
    print("py_cmp", x, y)
    return x - y

lib = ctypes.CDLL('./libsample.so')
lib.qsort.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_int, CMPFUNC)
lib.qsort(array, 5, ctypes.sizeof(ctypes.c_int), CMPFUNC(py_cmp))
print(array)

# Test ctypes.PYFUNCTYPE
PYFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)
lib.qsort.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_int, PYFUNC)
lib.qsort(array, 5
