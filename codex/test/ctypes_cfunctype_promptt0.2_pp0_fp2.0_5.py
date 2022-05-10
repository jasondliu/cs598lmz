import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# The following line is needed to make the test work on Windows.
# Without it, the function pointer is not correctly initialized.
