import ctypes
# Test ctypes.CFUNCTYPE
#
# This tests that ctypes.CFUNCTYPE works for all calling conventions,
# and that it creates callable function pointers, that are callable
# from C.

import sys
from ctypes import *

if sizeof(c_void_p) == 4:
    ERROR_PREFIX = "Error on 32-bit platform: "
else:
    ERROR_PREFIX = "Error on 64-bit platform: "

def test_cdecl(functype):
    # cdecl calling convention
    func = functype(lambda x: x + 1, use_errno=False)
    if func(1) != 2:
        raise Exception(ERROR_PREFIX + "cdecl")
    if func(-1) != 0:
        raise Exception(ERROR_PREFIX + "cdecl")

def test_stdcall(functype):
    # stdcall calling convention
    func = functype(lambda x: x + 1, "stdcall", use_errno=False)
