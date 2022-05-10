import ctypes
# Test ctypes.CFUNCTYPE()
# Test tp_call flag.
# Test only defaults arguments.

import _ctypes_test
dll = ctypes.CDLL(_ctypes_test.__file__)
