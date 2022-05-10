import ctypes
# Test ctypes.CFUNCTYPE
#
# ctypes.CFUNCTYPE is a metaclass.
#
# All it does is to call the constructor of the _CFuncPtr class,
# but it does it in a way that allows subclasses to override
# the _CFuncPtr class.

# XXX This test should be improved, it's a bit of a hack.

import _ctypes_test

class X(ctypes.CFUNCTYPE):
    _argtypes_ = (_ctypes_test.SP, )
    _restype_ = ctypes.c_int

class Y(ctypes.CFUNCTYPE):
    _argtypes_ = (_ctypes_test.SP, )
    _restype_ = ctypes.c_int

# X and Y are CFUNCTYPE classes, with different _CFuncPtr classes
# which are derived from _ctypes.CFuncPtr
#
# We create functions of type X and Y, and pass them to a function
# which expects a function pointer of the _ctypes.CFuncPtr type
#
# This works because X and Y are
