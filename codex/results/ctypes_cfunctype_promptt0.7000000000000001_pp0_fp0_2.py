import ctypes
# Test ctypes.CFUNCTYPE for Python callbacks
#
# This is a proof of concept for a new ctypes feature.
# It may not compile on your system, and it is not
# part of the ctypes API.
#
# The idea:
#
# A Python function can be passed as a function pointer to
# a C function.  This is a nice feature, but there are some
# things to watch out for:
#
# 1. The Python function must be callable with the C calling
#    convention.  This means that it must accept only
#    primitive types and structs as arguments.
#
# 2. The C code must not call the Python function directly, but
#    must call it through a proxy function.  This proxy function
#    is created by ctypes, and is also callable with the C
#    calling convention.
#
# 3. The Python function must not call any C functions.  This
#    is because the C calling convention is different from the
#    Python calling convention.  The Python function is currently
#    not allowed to call the C function, but calling C functions
#    from the Python function is
