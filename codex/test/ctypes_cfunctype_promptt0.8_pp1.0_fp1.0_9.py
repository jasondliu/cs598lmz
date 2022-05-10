import ctypes
# Test ctypes.CFUNCTYPE

try:
    from ctypes import CFUNCTYPE
except (ImportError, AttributeError):
    import sys
    print("SKIP")
    sys.exit()


functype = CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@functype
def double(i):
    return i * 2

