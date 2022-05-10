import ctypes
# Test ctypes.CFUNCTYPE(None)

def func():
    pass

c_func = ctypes.CFUNCTYPE(None)(func)

