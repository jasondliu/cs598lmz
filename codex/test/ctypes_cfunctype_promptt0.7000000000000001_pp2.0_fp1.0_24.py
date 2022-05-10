import ctypes
# Test ctypes.CFUNCTYPE

@ctypes.CFUNCTYPE(None)
def func():
    return 1

# @ctypes.WINFUNCTYPE(None)
