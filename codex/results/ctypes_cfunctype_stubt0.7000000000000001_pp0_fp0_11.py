import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return 5
print fun()

print '\n# Referencing a foreign function'
from ctypes import *
libc = CDLL(None)
libc.printf(b"Hello, %s!\n", b"world")

print '\n# Using a callback function'
from ctypes import *
libc = CDLL(None)

# Define a prototype for the callback function
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

# Define a Python function to use as the callback
def py_cmp_func(a, b):
    print("py_cmp_func({}, {}) was called".format(a, b))
    return a - b

# Convert the Python function into a C callback
cmp_func = CMPFUNC(py_cmp_func)

# Pass the C callback into a foreign function
libc.qsort(
    c_int64(id(b"example string")),
    c_size_t(1),
    c_size_t(sys.getsizeof(
