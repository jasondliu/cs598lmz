import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    """Test ctypes.CFUNCTYPE"""
    def func(x):
        return x * 2
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
    assert f(2) == 4

# Test ctypes.byref
def test_byref():
    """Test ctypes.byref"""
    x = ctypes.c_int()
    x.value = 42
    assert ctypes.byref(x).contents.value == 42

# Test ctypes.cast
def test_cast():
    """Test ctypes.cast"""
    x = ctypes.c_int()
    x.value = 42
    assert ctypes.cast(ctypes.pointer(x), ctypes.POINTER(ctypes.c_char)).contents.value == '*'

# Test ctypes.pointer
def test_pointer():
    """Test ctypes.pointer"""
    x = ctypes.c_int()
    x.value = 42
   
