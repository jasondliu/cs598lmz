import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

try:
    import _ctypes_test
except ImportError:
    raise ImportError("This test requires _ctypes_test module")

