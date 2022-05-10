import ctypes
# Test ctypes.CFUNCTYPE
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# Create a C callable function from a Python callable.
# restype: The result type.
# argtypes: A list of argument types.
# use_errno: If True, the function will check for the error indicator
# errno after calling the function, and throw an OSError exception
# if the indicator is non-zero.
# use_last_error: If True, the function will check for the error
# indicator GetLastError() after calling the function, and throw a
# WindowsError exception if the indicator is non-zero.
#
# Create a prototype of the function we want to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Convert the Python integer to a c integer and back
def py_int_to_c_int(i):
    return ctypes.c_int(i).value

# Convert the Python integer to a c integer and back
def py_
