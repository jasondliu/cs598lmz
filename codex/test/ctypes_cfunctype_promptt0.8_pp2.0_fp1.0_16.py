import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)
