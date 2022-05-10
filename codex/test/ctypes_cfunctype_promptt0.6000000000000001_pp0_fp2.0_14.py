import ctypes
# Test ctypes.CFUNCTYPE
#
# A function prototype is created as a C function pointer type,
# then passed to ctypes.CFUNCTYPE to create a Python callable.
#
# The ctypes.CFUNCTYPE is called with the result type of the
# function, and the types of the arguments.
#
# The resulting object is a callable Python object, which when
# called, will call the C function.
#
# The C function is passed a pointer to a ctypes.c_int, and
# returns a ctypes.c_int.
#
# The Python function also has a ctypes.c_int as return and
# argument type.
#
# The argument is passed as a pointer to a ctypes.c_int.
#
# The Python function returns the value of the c_int passed
# to it.

# C code:
#
# int c_testfunc(int *a) {
#   return *a;
# }

# Create a C function pointer type, with one int argument, and
# int return type.
