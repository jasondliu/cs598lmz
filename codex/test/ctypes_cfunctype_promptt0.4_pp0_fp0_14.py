import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
#
# This is a function pointer, and the function is defined in C.
#
# The function is defined as:
#
# int f(int x) { return x+1; }
#
# The return type, argument types, and calling convention are all
# specified in the CFUNCTYPE call.
#
# The function is called by a C function.  The C function is defined
# as:
#
# int g(int (*f)(int)) { return f(1); }
#
# The argument is a function pointer.  The return type, argument type,
# and calling convention are all specified in the ctypes.cdll.LoadLibrary
# call.
#
# The C function is called from Python.  The return type, argument type,
# and calling convention are all specified in the ctypes.cdll.LoadLibrary
# call.
#
# The C function is called from Python.  The return type, argument type,
# and calling convention are all specified in the ctypes.cdll.LoadLibrary
# call
