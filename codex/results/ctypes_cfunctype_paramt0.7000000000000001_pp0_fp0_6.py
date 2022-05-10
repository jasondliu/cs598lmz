import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint64)

def test_return_empty():
    test_func = FUNTYPE(lambda: None)
    assert test_func() == 0

def test_return_zero():
    test_func = FUNTYPE(lambda: 0)
    assert test_func() == 0

def test_return_one():
    test_func = FUNTYPE(lambda: 1)
    assert test_func() == 1

def test_return_constant():
    test_func = FUNTYPE(lambda: 0x1234567890ABCDEF)
    assert test_func() == 0x1234567890ABCDEF
