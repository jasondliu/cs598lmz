import ctypes
# Test ctypes.CFUNCTYPE

import os
import sys
import unittest

from ctypes import *

class CFunctionTypeTestCase(unittest.TestCase):

    def test_argtypes(self):
        if sys.platform == "win32":
            windll.kernel32.GetVersion.argtypes = None
            windll.kernel32.GetVersion.argtypes = (POINTER(DWORD),)

    def test_restype(self):
        if sys.platform == "win32":
            windll.kernel32.GetVersion.restype = None
            windll.kernel32.GetVersion.restype = DWORD

    def test_errcheck(self):
        if sys.platform == "win32":
            windll.kernel32.GetVersion.errcheck = None
            windll.kernel32.GetVersion.errcheck = lambda result, func, args: result

    def test_callconv(self):
        if sys.platform == "win32":
            windll.kernel32.GetVersion.callconv = None
            windll.kernel32.GetVersion.callconv = WINFUN
