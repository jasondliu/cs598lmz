import ctypes
# Test ctypes.CFUNCTYPE()

def _test_cfunctype_1():
    """
    >>> _test_cfunctype_1()
    1
    """
    c_func = ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: x + 1)
    return c_func(0)

def _test_cfunctype_2():
    """
    >>> _test_cfunctype_2()
    1
    """
    c_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
    return c_func(0)

def _test_cfunctype_3():
    """
    >>> _test_cfunctype_3()
    1
    """
    c_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y: x + y)
    return c_func(0, 1)

