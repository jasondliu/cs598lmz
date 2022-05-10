import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *

# This is a test for the ctypes.CFUNCTYPE factory function.
#
# The function takes a callable, and returns a new callable
# which calls the original callable, passing a tuple of
# arguments as a single parameter.
#
# The tuple contains the arguments passed to the new callable,
# converted to C data types according to the restype and argtypes
# attributes.

# The new callable has the same name and docstring as the original
# callable.

# The new callable has a restype and argtypes attributes, which
# can be set to a type or a sequence of types.

# The restype attribute specifies the type of the return value.

# The argtypes attribute specifies the types of the arguments.

# These attributes can be set before or after the callable is called.

# The new callable can be called with any kind of argument, Python
# objects as well as ctypes instances.

# The new callable raises a TypeError if the return value cannot be
# converted to the specified restype.

# The
