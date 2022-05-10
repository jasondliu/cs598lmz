import ctypes
# Test ctypes.CFUNCTYPE()
def func(x):
    return x

# Use ctypes.CFUNCTYPE() to create a function pointer type
# that takes one argument of type c_int and returns c_int.
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Convert func() to a function pointer.
cmp_func = CMPFUNC(func)

# Call the function pointer.
ret = cmp_func(1)
print(ret)

# Test passing a function pointer to a C function.
def print_int(x):
    print(x)

# Define a prototype for the C function.
PRINTFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int)

# Load the C library.
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Call the C function.
libc.qsort(ctypes.c_void_p(0), 0, 0, PRINTFUNC(print_int
