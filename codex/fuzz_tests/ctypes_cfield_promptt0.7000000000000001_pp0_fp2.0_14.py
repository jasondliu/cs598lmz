import ctypes
# Test ctypes.CField

import sys
import _testcapi

def test(test, func):
    test.startTest(func)
    func()
    test.testDone()

class CTest(unittest.TestCase):

    def test_Basic_CField(self):
        class X(ctypes.Structure):
            pass
        X._fields_ = [('n', ctypes.c_int),
                      ('s', ctypes.c_char_p)]
        x = X()
        x.n = 1
        x.s = b"hello"

        self.assertEqual(x.n, 1)
        self.assertEqual(x.s, b"hello")
        self.assertEqual(x.n, 1)
        self.assertEqual(x.s, b"hello")

    def test_CField_byref_to_int(self):
        class X(ctypes.Structure):
            pass
        X._fields_ = [('n', ctypes.c_int)]
        x = X()
        x.n = 1

