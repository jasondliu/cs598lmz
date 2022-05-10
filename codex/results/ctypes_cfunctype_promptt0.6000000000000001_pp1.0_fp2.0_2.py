import ctypes
# Test ctypes.CFUNCTYPE()

# The data types used in the function prototype are used to create the type
# object.

# The function prototype is 'int foo(int, int)'.
# The argtypes is 'i' (int), 'i' (int).
# The restype is 'i' (int).

import sys
import _ctypes_test

lib = _ctypes_test.dll

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

# If argtypes is a tuple, and the restype is not None
