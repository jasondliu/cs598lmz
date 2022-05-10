import ctypes
# Test ctypes.CFUNCTYPE by declaring and calling a function.
#
# This is a demonstration of the simplest use of CFUNCTYPE:
# defining a C function pointer and calling it.

# define a C function pointer type for a function taking a
# double, returning a double.
cfunc_type = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# define a C function that takes a double and returns a double.
@cfunc_type
def c_sin(x):
    return math.sin(x)

# call the C function.
print(c_sin(1.0))

# define a C function pointer type for a function taking a
# double and a pointer to a double, returning a void.
cfunc_type = ctypes.CFUNCTYPE(None, ctypes.c_double, ctypes.POINTER(ctypes.c_double))

# define a C function that takes a double and a pointer to a
# double, and sets the value of the double pointed to.
@cfunc_type
def c_sin_to_
