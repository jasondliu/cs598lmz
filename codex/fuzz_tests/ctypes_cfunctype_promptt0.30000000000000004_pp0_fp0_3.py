import ctypes
# Test ctypes.CFUNCTYPE(None)
def test_CFUNCTYPE_None():
    try:
        ctypes.CFUNCTYPE(None)
    except TypeError:
        pass
    else:
        raise Exception("should have raised TypeError")

# Test ctypes.CFUNCTYPE(ctypes.c_int)
def test_CFUNCTYPE_c_int():
    try:
        ctypes.CFUNCTYPE(ctypes.c_int)
    except TypeError:
        pass
    else:
        raise Exception("should have raised TypeError")

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def test_CFUNCTYPE_c_int_c_int():
    try:
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    except TypeError:
        pass
    else:
        raise Exception("should have raised TypeError")

# Test ctypes.CFUNCTYPE(ctypes.c_int, c
