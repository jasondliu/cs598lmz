import ctypes
# Test ctypes.CFUNCTYPE()
CFUNCTYPE = ctypes.CFUNCTYPE

@CFUNCTYPE(None)
def func():
    pass

# Test ctypes.POINTER()
POINTER = ctypes.POINTER

