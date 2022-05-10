import ctypes
# Test ctypes.CFUNCTYPE
#
# CFUNCTYPE(result, args...)
#
# where result is the ctypes type for the result, and args is a tuple of
# ctypes types for the arguments.
#
# The function prototype is the same as the prototype of a C function
# pointer.
#
# If the result is a simple ctypes type, the function returns a Python
# integer or float.  If the result is a structure or union, the function
# returns an instance of the class wrapping the structure or union.
#
# If the result is a pointer, the function returns a ctypes instance,
# normally a c_char_p instance.
#
# If the result is a c_char_p, the function returns a Python string.
#
# If the result is a c_wchar_p, the function returns a Python unicode
# string.
#
# If the result is a c_void_p, the function returns a Python integer
# representing the pointer value.  This is not a memory address, it's
# just an integer.
#
# If the result is a pointer to a function, the function
