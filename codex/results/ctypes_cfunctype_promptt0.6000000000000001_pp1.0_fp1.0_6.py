import ctypes
# Test ctypes.CFUNCTYPE(None)
def test_CFUNCTYPE_None():
    import _ctypes_test
    d = ctypes.CFUNCTYPE(None)(_ctypes_test.get_pointee)
    assert d() is None

# Test ctypes.CFUNCTYPE(SomeInteger)
def test_CFUNCTYPE_SomeInteger():
    import _ctypes_test
    d = ctypes.CFUNCTYPE(ctypes.c_short)(_ctypes_test.get_pointee)
    res = d()
    assert res == ctypes.c_short(1234).value

# Test ctypes.CFUNCTYPE(ctypes.c_int)
def test_CFUNCTYPE_c_int():
    import _ctypes_test
    d = ctypes.CFUNCTYPE(ctypes.c_int)(_ctypes_test.get_pointee)
    res = d()
    assert res == ctypes.c_int(1234).value

# Test ctypes.CFUNCTYPE(ct
