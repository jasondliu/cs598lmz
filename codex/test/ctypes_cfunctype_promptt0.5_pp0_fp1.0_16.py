import ctypes
# Test ctypes.CFUNCTYPE(...)

# Test that all the argument types are supported
def test_CFUNCTYPE_all_arg_types():
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)

