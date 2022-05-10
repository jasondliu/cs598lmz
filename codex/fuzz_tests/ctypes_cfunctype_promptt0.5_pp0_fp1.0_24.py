import ctypes
# Test ctypes.CFUNCTYPE(None)
#

import _ctypes_test

if _ctypes_test.get_type('f') != ctypes.CFUNCTYPE(None):
    raise RuntimeError("CFUNCTYPE(None) is not compatible with f")

f = ctypes.CFUNCTYPE(None)(lambda: 3)
f()
