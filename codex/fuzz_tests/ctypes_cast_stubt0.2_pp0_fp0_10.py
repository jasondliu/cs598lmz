import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a way to get the value of a null pointer, but it's
# kind of a hack.

# The ctypes documentation for Python 2.5 says:
#
#     Note that c_void_p(None) is different from
#     cast(None, c_void_p).  The latter creates a NULL pointer,
#     the former a pointer to None.
#
# The documentation for Python 2.6 says:
#
#     Note that c_void_p(None) is different from
#     cast(None, c_void_p).  The latter creates a NULL pointer,
#     while the former is a pointer to a Python integer object
#     (the value 0).
#
# The documentation for Python 2.7 says:
#
#     Note that c_void_p(None) is different from
#     cast(None, c_void_p).  The latter creates a NULL pointer,
#     while the former is a pointer to a Python integer object
#     (the value 0).
#
# The documentation for Python
