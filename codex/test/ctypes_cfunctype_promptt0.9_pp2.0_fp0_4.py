import ctypes
# Test ctypes.CFUNCTYPE()

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def test_func(a, b):
    return a + b


# Call function
