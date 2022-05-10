import ctypes
# Test ctypes.CFUNCTYPE(), type map, and argtype

import os
import sys
from ctypes import *

old_stdout = sys.stdout
sys.stdout = open(test.test_support.TESTFN, 'w')

try:
    LONG = c_long
except NameError:
    LONG = c_int

GetLastError = windll.kernel32.GetLastError
GetLastError.argtypes = []
GetLastError.restype = LONG

SetLastError = windll.kernel32.SetLastError
SetLastError.argtypes = [LONG]
SetLastError.restype = None

CreateFileA = windll.kernel32.CreateFileA
CreateFileA.argtypes = [LPCSTR, DWORD, DWORD, c_void_p, DWORD, DWORD, HANDLE]
CreateFileA.restype = HANDLE
CreateFileA.errcheck = lambda res, func, args: (
    None if res != HANDLE(-1).value else GetLastError() )

def errcheck_zero(result, func, args):

