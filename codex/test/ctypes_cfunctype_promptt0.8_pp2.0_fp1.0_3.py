import ctypes
# Test ctypes.CFUNCTYPE
def my_callback(a, b):
    print (a, b)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

