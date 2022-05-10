import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def test(name, restype, argtypes):
    func = CFUNCTYPE(restype, *argtypes)
