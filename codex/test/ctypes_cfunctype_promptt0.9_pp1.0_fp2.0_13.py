import ctypes
# Test ctypes.CFUNCTYPE() as a result of a call

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)
