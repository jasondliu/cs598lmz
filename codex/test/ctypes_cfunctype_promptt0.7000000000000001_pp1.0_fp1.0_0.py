import ctypes
# Test ctypes.CFUNCTYPE
#
# A ctypes callback is a Python object that is called when a
# C function pointer is invoked.  This is useful for implementing
# C callbacks, for example for an asynchronous notification, or
# a C library function taking a function pointer argument.
#
# This test demonstrates that ctypes callback functions work.
#
import _ctypes_test
