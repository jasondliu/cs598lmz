import ctypes
# Test ctypes.CFUNCTYPE
#
# The ctypes.CFUNCTYPE factory function creates callable C function pointers
# from Python callables.
#
# The first argument to CFUNCTYPE is the return type of the function.  The
# rest of the arguments are the argument types.  The argument types may be
# ctypes types, or may be Python callables that return a ctypes type, such as
# a Structure or Union subclass.
#
# The callable returned by CFUNCTYPE takes the same arguments as the Python
# callable, and returns the same value, with the following exceptions:
#
# 1. If the return type is a primitive type, the value is automatically
#    converted to the return type.
#
# 2. If the return type is a Structure or Union subclass, an instance of the
#    subclass is returned.
#
# 3. If the return type is a pointer type, a ctypes instance is returned.
#    This instance can be passed to functions expecting the corresponding
#    argument type.  If the pointer refers to a C structure, the contents of
#    the structure can be accessed as attributes of
