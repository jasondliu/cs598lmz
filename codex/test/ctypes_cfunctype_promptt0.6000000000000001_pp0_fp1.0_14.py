import ctypes
# Test ctypes.CFUNCTYPE
#
#     void (*func)(void)
#
import _ctypes_test

try:
    import _ctypes_test
except ImportError:
    raise Exception("import _ctypes_test failed")

