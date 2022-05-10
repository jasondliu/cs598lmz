import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# The CFUNCTYPE() constructor creates a prototype object, which is
# used to create callable C functions.
#
# The prototype object is callable, and creates real C function
# objects.

# The CFUNCTYPE() constructor takes a number of arguments, the
# first one being the return type, the rest the argument types.
#
# The argument types are C data types, such as ctypes.c_int, or
# ctypes.c_double.

# The return type can be None, or any C data type.

# The C function is created by calling the prototype object.

# The prototype object can be called with any number of arguments,
# as long as the number and types of the arguments are compatible
# with the prototype.

# The C function object is callable, and takes the same arguments
# as the prototype object.

# The C function object is also a callable class instance, so you
# can call the C function both as a function
