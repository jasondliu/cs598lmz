import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    # Test calling a function pointer
    def func(x):
        return x + 1
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
    assert f(1) == 2
    # Test calling a callback
    def callback(x):
        return x + 1
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(callback)
    assert f(1) == 2
    # Test calling a callback with a different argument type
    def callback(x):
        return x + 1
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)(callback)
    assert f(1) == 2
    # Test calling a callback with a different return type
    def callback(x):
        return x + 1
    f = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)(callback)
    assert f(1) == 2
   
