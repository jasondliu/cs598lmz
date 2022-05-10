import ctypes
# Test ctypes.CFUNCTYPE()

# Test ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# Create a function prototype, similar to the C declaration:
#   restype func(argtype, argtype, ...)
#
# restype: The result type of the function.  This must be a ctypes type,
#      or something that can be converted into a ctypes type, like a
#      Python type object.  If restype is None, the restype of the
#      function is int.
# argtypes: A list of argtypes. Each argtype must be a ctypes type or
#      something that can be converted into a ctypes type.  If no
#      argtypes are given, the function is assumed to take no
#      arguments.
# use_errno: If use_errno is True, and the function fails, ctypes will
#      check errno and raise an OSError exception if it is non-zero.
# use_last_error: If use_last_error is True, and the function fails,

