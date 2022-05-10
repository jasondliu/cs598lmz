import ctypes
# Test ctypes.CFUNCTYPE with a None return type (this should be void).

import _ctypes_test
lib = ctypes.CDLL(_ctypes_test.__file__)

# None is the same as void:
