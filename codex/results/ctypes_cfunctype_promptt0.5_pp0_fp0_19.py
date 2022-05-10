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
_libraries['libtest_ctypes_callbacks_functions.so'] = ctypes.CDLL('libtest_ctypes_callbacks_functions.so')

call_function = _libraries['libtest_ctypes_callbacks_functions.so'].call_function
call_function.argtypes = [FunctionType, ctypes.c_int]
call_function.restype = None

# This function definition should be moved to a header file,
# when we start to support header files in ctypesgen.
#
# int call_function_with_return(
