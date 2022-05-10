import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    """
    >>> test_CFUNCTYPE()
    1
    """
    import ctypes
    c_int_p = ctypes.POINTER(ctypes.c_int)
    c_int_p_p = ctypes.POINTER(c_int_p)
    def func(a, b):
        return a + b
    FUNC = ctypes.CFUNCTYPE(ctypes.c_int, c_int_p, c_int_p)
    f = FUNC(func)
    a = c_int_p(ctypes.c_int(1))
    b = c_int_p(ctypes.c_int(2))
    return f(a, b)

# Test ctypes.byref
def test_byref():
    """
    >>> test_byref()
    1
    """
    import ctypes
    c_int_p = ctypes.POINTER(ctypes.c_int)
    c_int_p_p = ctypes.PO
