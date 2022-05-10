import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test_cfuntype_c_int_c_int():
    """
    >>> def my_callback(x):
    ...     return x+1
    >>> cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(my_callback)
    >>> cb(10)
    11
    """

def test_cfuntype_c_int_c_void_p():
    """
    >>> def my_callback(x):
    ...     return x+1
    >>> cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_callback)
    >>> cb(10)
    11
    """

def test_cfuntype_c_int_c_char_p():
    """
    >>> def my_callback(x):
    ...     return x+1
    >>> cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c
