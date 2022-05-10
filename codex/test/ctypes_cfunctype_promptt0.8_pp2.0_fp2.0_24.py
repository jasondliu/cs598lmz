import ctypes
# Test ctypes.CFUNCTYPE.
#
# ctypes does not support arrays passed by value. The data must be passed
# as a pointer to a fixed size buffer.
#

import ctypes, _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

