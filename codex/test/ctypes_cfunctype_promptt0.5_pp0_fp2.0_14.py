import ctypes
# Test ctypes.CFUNCTYPE
#
# The CFUNCTYPE is the same as CFUNCTYPE(None),
# except that it uses a default argument instead of a keyword argument.
#
# CPython issue #18667: ctypes.CFUNCTYPE(None, ...) is broken.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

