import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
#
#  PyPy's ctypes
#
# ___________________________________________________________________________

# PyPy's ctypes is a reimplementation of CPython's ctypes.
# It is a fairly thin layer on top of the internal API.

from ctypes import *

# ___________________________________________________________________________
#
#  ctypes.c_int, ctypes.c_void_p
#
# ___________________________________________________________________________

# These are the most important types.
# They are used to represent the C int and void* types.
#
# ctypes.c_int is a subclass of rffi.r_longlong.
# It is used to represent the C int type.
#
# ctypes.c_void_p is a subclass of rffi.r_longlong.
# It is used to represent the C void* type.
#
# The following functions are used to convert between
# ctypes.c_int and ctypes.c_void_p instances and
# rffi.r_longlong instances.

