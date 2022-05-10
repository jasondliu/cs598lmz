import ctypes
# Test ctypes.CFUNCTYPE()

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def test_func(a, b):
    return a + b


# Call function
print test_func(1,2)
# Add aditional args
# Throws error
print test_func(1, 2, 3)
