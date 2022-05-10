import ctypes
# Test ctypes.CFUNCTYPE
#
# http://www.tutorialspoint.com/python/python_c_extensions.htm
#
# NOTE: not all C data types are supported.
#
# NOTE: ctypes.CFUNCTYPE is a callable class.
#
# NOTE: ctypes.CFUNCTYPE(result, *args)
#       result: the return type of the callback function
#       args: a sequence of argument types
#
# NOTE: ctypes.CFUNCTYPE(result, *args)(python_callable)
#       python_callable: a Python callable object (such as a function)
#
# NOTE: the callback function must be defined with the __stdcall__ attribute
#
# NOTE: the callback function must use ctypes.c_char_p instead of str
#
# NOTE: the callback function must use ctypes.c_void_p instead of None
#
# NOTE: the callback function can use None instead of ctypes.c_void_p
#
# NOTE: the callback function can use None instead of ctypes.c_int
#
# NOTE
