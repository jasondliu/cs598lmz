import ctypes
# Test ctypes.CFUNCTYPE
# See https://docs.python.org/3.5/library/ctypes.html#ctypes.CFUNCTYPE

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# creates a C callable function prototype instance.
#
# restype is the result type, which can be a ctypes type or a Python callable.
# argtypes is a tuple of argument types.
# 
# The use_errno and use_last_error arguments are quite obscure.
# They are used to control how the function looks at the global error
# indicator variables: errno (use_errno) and GetLastError() /
# GetLastError() (use_last_error).

# The return type can be a ctypes type or a Python callable.
# If it is a ctypes type, the function result value is interpreted
# as that type. If it is a Python callable, it is called with the
# function result as the only parameter. If the callable returns
# a value, this value is used as
