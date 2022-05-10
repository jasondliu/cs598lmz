import ctypes
# Test ctypes.CFUNCTYPE
#
# The CFUNCTYPE() function creates a C function pointer type
# from a Python callable.
#
# The first argument to CFUNCTYPE() is the return type of the
# function.  The rest of the arguments are the types of the
# function's arguments.
#
# The returned type object can be used as the restype or argtypes
# attributes of the C function object.
#
# The returned type object can also be passed as the first
# argument to the CDLL() function to load a foreign library.
#
# The returned type object can also be passed as the first
# argument to the WinDLL() function to load a foreign library.
#
# The returned type object can also be passed as the first
# argument to the OleDLL() function to load a foreign library.
#
# The returned type object can also be passed as the first
# argument to the GetProcAddress() function to load a foreign
# function.
#
# The returned type object can also be passed as the first
# argument to the cast() function to cast a foreign function
# pointer to a Python object
