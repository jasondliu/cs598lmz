import ctypes
# Test ctypes.CFUNCTYPE

def test_CFUNCTYPE_0():
    """Test CFUNCTYPE(None)"""
    f = ctypes.CFUNCTYPE(None)(lambda: None)
    f()

def test_CFUNCTYPE_1():
    """Test CFUNCTYPE(c_int, c_int)"""
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
    assert f(42) == 42

def test_CFUNCTYPE_2():
    """Test CFUNCTYPE(None, c_int)"""
    f = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)
    f(42)

def test_CFUNCTYPE_3():
    """Test CFUNCTYPE(c_int, c_int, c_int)"""
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(
