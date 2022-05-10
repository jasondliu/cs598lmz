import ctypes
# Test ctypes.CFUNCTYPE.

import _ctypes_test

lib = ctypes.cdll.LoadLibrary(_ctypes_test.__file__)

#char func(char, char)
