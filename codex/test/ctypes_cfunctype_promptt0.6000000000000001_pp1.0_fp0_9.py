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

