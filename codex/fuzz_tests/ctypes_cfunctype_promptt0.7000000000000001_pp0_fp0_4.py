import ctypes
# Test ctypes.CFUNCTYPE.
#
# The ctypes module can be used to create C callback functions in Python.
#
# The CFUNCTYPE factory function creates a C callable function prototype.
# The first argument is the return type, followed by the types of the
# arguments. For example, the following defines a C function type that
# accepts a double argument and returns an int.
#
#     int_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)
#
# This function type can then be used as an argument type to another C
# function using the restype and argtypes attributes. For example, the
# following defines a C function that accepts a function pointer.
#
#     prototype = ctypes.CFUNCTYPE(None, ctypes.c_double, int_func)
#
#     def myfunc(val, func):
#         if func(val) != 0:
#             print('Bad value', val)
#
#     cfunc = prototype(myfunc)
#
# The myfunc function can now be passed to another C function that

