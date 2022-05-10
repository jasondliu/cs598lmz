import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    """
    >>> def cb(a, b):
    ...     print(a, b)
    ...     return a + b
    >>> cb_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(cb)
    >>> cb_c(1, 2)
    1 2
    3
    """

# Test ctypes.POINTER
