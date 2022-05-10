import ctypes
# Test ctypes.CFUNCTYPE(...)

def POINT(i):
    return ctypes.c_int16(i).value

FPTR = ctypes.CFUNCTYPE(None, ctypes.c_int16)

def callback(i):
    print("callback", i)

fptr = FPTR(callback)
fptr(POINT(123))

def callback2(i):
    print("callback2", i)

fptr = FPTR(callback2)
fptr(POINT(456))

def callback3(i):
    print("callback3", i)
    raise Exception

fptr = FPTR(callback3)
fptr(POINT(456))

import unittest

class TestPassingFunctions(unittest.TestCase):
    def test_win_function(self):
        from ctypes import POINTER, c_void_p, c_int
        from ctypes.wintypes import BOOL, HWND, UINT, WPARAM, LPARAM
