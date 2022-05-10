import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    """
    >>> py.test.skip("XXX Fixme")
    >>> cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    >>> cb(1, 2)
    3
    >>> cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    >>> cb(4)
    4
    >>> cb.restype = ctypes.c_int
    >>> cb.restype
    <class '__main__.c_int'>
    >>> cb(4)
    4
    >>> cb.argtypes = [ctypes.c_int, ctypes.c_int]
    >>> cb.argtypes
    [<class '__main__.c_int'>, <class '__main__.c_int'>]
    >>> cb(1, 2)
    3
    """

# Test ctypes.byref()
