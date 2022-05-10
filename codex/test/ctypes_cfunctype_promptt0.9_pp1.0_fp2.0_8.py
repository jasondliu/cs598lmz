import ctypes
# Test ctypes.CFUNCTYPE on a simple python function
#
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char)
def add2(ch):
    return ord(ch) + 2

