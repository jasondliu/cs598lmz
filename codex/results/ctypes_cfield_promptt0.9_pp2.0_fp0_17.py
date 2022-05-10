import ctypes
# Test ctypes.CField.offset - HPUX version
import ctypes.test.test_cfield
import unittest

class Test(unittest.TestCase):
    def runTest(self):
        self.failUnlessEqual(ctypes.CField.offset, ctypes.CField.offset)


if __name__ == "__main__":
    unittest.main()
