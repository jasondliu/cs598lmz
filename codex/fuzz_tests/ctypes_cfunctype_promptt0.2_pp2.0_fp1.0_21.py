import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call_function takes a function pointer as first argument, and
# calls it with the remaining arguments.
call_function = lib.call_function
call_function.argtypes = [ctypes.c_void_p] + [ctypes.c_int] * 9
call_function.restype = ctypes.c_int

# call_function_obj takes a function object as first argument, and
# calls it with the remaining arguments.
call_function_obj = lib.call_function_obj
call_function_obj.argtypes = [ctypes.py_object] + [ctypes.c_int] * 9
call_function_obj.restype = ctypes.c_int

# call_function_obj takes a function object as first argument, and
# calls it with the remaining arguments.
call_function_use_errno = lib.call_function_use_errno
call_function_use_errno.argtypes = [ctypes.py_object
