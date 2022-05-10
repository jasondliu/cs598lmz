import ctypes
# Test ctypes.CFUNCTYPE on several functions.
from ctypes import *
import _ctypes_test

def test(restype, argtypes, *args):
    @CFUNCTYPE(restype, *argtypes)
    def func(*args):
        return args[0] * args[1]

    func.argtypes = argtypes
    func.restype = restype

    res = func(*args)
    if res != args[0] * args[1]:
        print(res)
        raise RuntimeError("CFUNCTYPE failed.")

for t in [c_int, c_void_p, c_char_p, c_wchar_p, py_object]:
    test(c_int, [t, c_int], t(3), 4)
    test(c_int, [c_int, t], 3, t(4))

# Test CFUNCTYPE(None)
@CFUNCTYPE(None, c_int)
def voidfunc(value):
    print("hello", value)

voidfunc(42)

# Test CFUNCT
