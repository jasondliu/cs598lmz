import ctypes
# Test ctypes.CFUNCTYPE.
#
# The following function definition should be moved to a header file,
# when we start to support header files in ctypesgen.
#
# typedef void (*FunctionType)(int);

FunctionType = ctypes.CFUNCTYPE(None, ctypes.c_int)

# This function definition should be moved to a header file,
# when we start to support header files in ctypesgen.
#
# void call_function(FunctionType func, int arg);

_libraries = {}
