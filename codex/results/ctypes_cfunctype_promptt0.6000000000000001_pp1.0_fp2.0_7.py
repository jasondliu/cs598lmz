import ctypes
# Test ctypes.CFUNCTYPE()
@CFUNCTYPE(c_int, c_int, c_int)
def add_test(a, b):
    return a + b

add_test(1, 2)

# Test ctypes.PYFUNCTYPE()
@PYFUNCTYPE(c_int, c_int, c_int)
def add_test(a, b):
    return a + b

add_test(1, 2)
