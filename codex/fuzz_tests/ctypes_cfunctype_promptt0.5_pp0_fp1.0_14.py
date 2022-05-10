import ctypes
# Test ctypes.CFUNCTYPE(None)
def test_CFUNCTYPE1():
    func_type = ctypes.CFUNCTYPE(None)
    assert func_type(lambda: None) is not None
    assert func_type(lambda: None)() is None
    assert func_type(lambda: None)() is None
    raises(TypeError, func_type, lambda: None, 42)
    raises(TypeError, func_type, lambda: None, 'hello')
    raises(TypeError, func_type, lambda: None, 'hello', 42)
    raises(TypeError, func_type, lambda: None, 'hello', 42, 42)
    raises(TypeError, func_type, lambda: None, 'hello', 42, 42, 42)
    raises(TypeError, func_type, lambda: None, 'hello', 42, 42, 42, 42)
    raises(TypeError, func_type, lambda: None, 'hello', 42, 42, 42, 42, 42)
    raises(TypeError, func_type, lambda: None, 'hello', 42, 42, 42, 42, 42
