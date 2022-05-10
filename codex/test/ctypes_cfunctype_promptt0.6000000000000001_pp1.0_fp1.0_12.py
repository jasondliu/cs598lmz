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

