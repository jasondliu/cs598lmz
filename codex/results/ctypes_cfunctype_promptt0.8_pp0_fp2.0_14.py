import ctypes
# Test ctypes.CFUNCTYPE arg0 is passed as a pointer to
# the value itself. 

from ctypes import *
from ctypes.wintypes import *
import _ctypes_test

user32 = windll.user32

def testfunc(arg0):
    print(arg0)
    if arg0 == 42:
        return True
    return False

CMPFUNC = WINFUNCTYPE(BOOL, c_int)
cmp_func = CMPFUNC(testfunc)

test_pointer = c_int(42)
assert testfunc(test_pointer.value) == True
assert testfunc(byref(test_pointer)) == True

_ctypes_test.LP_c_int.from_param(test_pointer)
_ctypes_test.LP_c_int.from_param(byref(test_pointer))

user32.EnumWindows(cmp_func, byref(test_pointer))
# user32.EnumWindows(cmp_func, test_pointer) # crashes the interpreter


if __name__ == "__main__":
    import
