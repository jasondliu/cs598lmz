import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    # Test function with no arguments and no return value
    def func_0_0():
        print("Running func_0_0")
        return 0
    cfunc_0_0 = ctypes.CFUNCTYPE(None)(func_0_0)
    assert cfunc_0_0() == None
    # Test function with one argument and no return value
    def func_1_0(a):
        print("Running func_1_0")
        assert a == 1
        return 0
    cfunc_1_0 = ctypes.CFUNCTYPE(None, ctypes.c_int)(func_1_0)
    assert cfunc_1_0(1) == None
    # Test function with two arguments and no return value
    def func_2_0(a, b):
        print("Running func_2_0")
        assert a == 1 and b == 2
        return 0
