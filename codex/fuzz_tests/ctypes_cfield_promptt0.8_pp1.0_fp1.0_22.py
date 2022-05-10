import ctypes
# Test ctypes.CField.from_address (without object ownership).
import unittest

class X(ctypes.Structure):
    pass

class BaseTestCase(unittest.TestCase):
    def test(self):
        p = ctypes.cast(ctypes.pointer(X()), ctypes.POINTER(ctypes.c_int))
        f = ctypes.CField.from_address(p, ctypes.c_int)
        self.assertIs(f.__class__, ctypes.CField)
        self.assertEqual(f.value, 0)
        f.value = 0x1234
        self.assertEqual(p[0], 0x1234)


if __name__ == "__main__":
    unittest.main()
