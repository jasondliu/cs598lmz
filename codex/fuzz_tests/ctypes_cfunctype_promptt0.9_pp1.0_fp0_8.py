import ctypes
# Test ctypes.CFUNCTYPE for a function that accepts a Python int.
def foo(x):
    print x

# create a prototype of the function we want,
fptr = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_long)
# the first paramet is the return value and the second paramet is the type of the parameter
# create a version of the function that accepts Python ints,
intfoo = fptr(foo)
# call it,
intfoo(42)
# now call it with some other type,


# ctypes.byref - return a ctypes object which is a pointer to the original object
# ctypes.byref(obj)[0] - return the value pointed to by the pointer, the first element of obj

# ctypes.pointer - create a ctypes pointer from a ctypes instance
# ctypes.cast - create a ctypes instance from a pointer

a = ctypes.c_int()
a.value = 5
ctypes.pointer(a).contents


import ctypes

# a pointer to integer
i = ctypes.c_int
