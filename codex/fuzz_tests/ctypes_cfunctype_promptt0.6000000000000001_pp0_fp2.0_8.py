import ctypes
# Test ctypes.CFUNCTYPE by declaring a function with CFUNCTYPE, and
# calling it.
#
# Test also ctypes.addressof, by passing a function created with
# CFUNCTYPE as an argument.

import sys
import unittest
from test import support

if sys.platform == "win32":
    # On Windows, the following declaration causes a crash in the
    # interpreter, because the "dllimport" attribute is not allowed
    # on data.  This is why it is commented out.
    #dllimport = ctypes.WINFUNCTYPE
    stdcall = ctypes.WINFUNCTYPE
    cdecl = ctypes.CFUNCTYPE
else:
    dllimport = ctypes.CFUNCTYPE
    stdcall = ctypes.CFUNCTYPE
    cdecl = ctypes.CFUNCTYPE


class CFuncPtrTestCase(unittest.TestCase):
    def test_call_int(self):
        @stdcall(ctypes.c_int, ctypes.c_int)
        def func(a):
           
