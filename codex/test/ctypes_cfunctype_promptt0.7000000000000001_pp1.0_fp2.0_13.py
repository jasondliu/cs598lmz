import ctypes
# Test ctypes.CFUNCTYPE

# It turns out that CFUNCTYPE doesn't always use a PyCFunction,
# but can use a CFUNCTYPE-based function instead, in which case
# the type of the arguments must be specified explicitly.

import _ctypes_test

