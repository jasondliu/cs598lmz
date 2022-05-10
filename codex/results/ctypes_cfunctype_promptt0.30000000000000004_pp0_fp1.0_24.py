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
def test_POINTER():
    """
    >>> c_int_p = ctypes.POINTER(ctypes.c_int)
    >>> c_int_p
    <class 'ctypes.LP_c_int'>
    >>> c_int_p(ctypes.c_int(42))
    c_long(42)
    >>> c_int_p(c_int_p(ctypes.c_int(42)))
    c_long(42)
    >>> c_int_p(ctypes.c_int(42)).contents
    c_long(42)
   
