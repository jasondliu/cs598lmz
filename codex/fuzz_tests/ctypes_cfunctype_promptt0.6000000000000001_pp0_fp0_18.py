import ctypes
# Test ctypes.CFUNCTYPE() with an integer return type and no arguments.
def test_1():
    import _ctypes_test
    callextern = ctypes.CFUNCTYPE(ctypes.c_int)(_ctypes_test.get_errno)
    res = callextern()
    if res != 0:
        raise ValueError("test_1 failed: the result should be 0")


# Test ctypes.CFUNCTYPE() with an integer return type and one integer
# argument.
def test_2():
    import _ctypes_test
    callextern = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(
        _ctypes_test.sum_ints)
    res = callextern(10)
    if res != 45:
        raise ValueError("test_2 failed: the result should be 45")


# Test ctypes.CFUNCTYPE() with an integer return type and two integer
# arguments.
def test_3():
    import _ctypes_test
    callextern = ctypes.CFUNCTY
