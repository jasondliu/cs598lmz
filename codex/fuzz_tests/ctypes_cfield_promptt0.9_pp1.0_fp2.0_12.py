import ctypes
# Test ctypes.CField with function.
# Verify that we get the same result as we would with a pointer to a struct.
from ctypes import c_byte, c_int

from ctypes import *
from ctypes.util import find_library

from _ctypes_test import func_types
msvcrt = find_library("msvcrt")
if msvcrt:
    msvcrt = cdll.msvcrt


class Bar:
    def __init__(self, val):
        self.val = val

    def test(self, bar):
        print(self.val, bar)


if hasattr(msvcrt, "malloc"):
    BarPtr = POINTER(Bar)
    malloc = msvcrt.malloc
    malloc.restype = BarPtr
    free = msvcrt.free
    free.argtypes = BarPtr,
    free.restype = None
    s = c_byte * 100

    def testfunc(bar):
        bar.contents.test(list(bar.contents.val))


    for
