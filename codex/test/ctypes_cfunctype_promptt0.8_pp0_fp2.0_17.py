import ctypes
# Test ctypes.CFUNCTYPE
def py_test_callback(a, b):
    print (a, b)

test_callback = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(py_test_callback)
