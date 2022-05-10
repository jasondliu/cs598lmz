import ctypes
# Test ctypes.CFUNCTYPE vs ctypes.WINFUNCTYPE on Windows.

from ctypes import *

def test_CFUNCTYPE():
    # This works.
    CallBackProc = CFUNCTYPE(c_int, c_int, c_int, c_int)
    print(CallBackProc)
    print(CallBackProc(5,5,5,5))

def test_WINFUNCTYPE():
    # This doesn't work.
    CallBackProc = WINFUNCTYPE(c_int, c_int, c_int, c_int)
    print(CallBackProc)
    print(CallBackProc(5,5,5,5))


