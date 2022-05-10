import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    """
    >>> test_CFUNCTYPE()
    1
    """
    c_int_p = ctypes.POINTER(ctypes.c_int)
    c_int_p_p = ctypes.POINTER(c_int_p)
    c_int_p_p_p = ctypes.POINTER(c_int_p_p)
    c_int_p_p_p_p = ctypes.POINTER(c_int_p_p_p)
    c_int_p_p_p_p_p = ctypes.POINTER(c_int_p_p_p_p)
    c_int_p_p_p_p_p_p = ctypes.POINTER(c_int_p_p_p_p_p)
    c_int_p_p_p_p_p_p_p = ctypes.POINTER(c_int_p_p_p_p_p_p)
    c_int_p_p_p_
