import ctypes
# Test ctypes.CFUNCTYPE (tuple as argument)

# This code is from Issue12656, which is now closed.

import unittest, sys
if sys.platform == "win32":
    import win32con
else:
    win32con = None


@unittest.skipUnless(win32con, "win32 only")
class TestCFUNCTYPE(unittest.TestCase):
    def test_cfunctype(self):
        # This test makes sure that CFUNCTYPE does now allow tuples
        f1a = lambda x: None
        f1b = lambda x: None
        f2  = lambda x, y: None
        f3  = lambda x, y, z: None
        f10 = lambda: None

        # Issue 12656 (fixed)
        #  First test all of the possible signatures
        self.assertRaises(TypeError, ctypes.CFUNCTYPE, (f1a,), ())
