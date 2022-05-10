import ctypes
# Test ctypes.CFUNCTYPE
#
# The CFUNCTYPE() function lets you define new C functions in Python.
# You give the CFUNCTYPE() function the result-type of the function
# and a tuple of the argument types.  You can also specify "varargs"
# in the argument type list.
#
# The function returns a callable object that can be called just like
# a normal Python function.  When the function is called, the Python
# arguments are converted to C data and passed to the C function.
# When the C function returns, the return value is converted to a
# Python object.
#
# Note that the callback functions are implemented in C, so they must
# follow the standard C calling convention.  This means that they
# must use the ctypes.c_int data type for their return value.

# This is the prototype of the C function we want to call
#
# int add(int, int);

# This creates a new C function type.  The first parameter is the
# return type, the second is a tuple of the argument types.
#
# Note that we can use None as a placeholder
