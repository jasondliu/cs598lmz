import ctypes
# Test ctypes.CFieldAsDict.
#
# Written by Yutaka Oiwa.

if __name__ == "__main__":
    import unittest
    from test_support import run_unittest

    class CFieldAsDictTest(unittest.TestCase):
        def test_c_field_as_dict(self):
            class X(ctypes.Structure):
                _fields_ = [('a', ctypes.c_int)]

            x = X()
            d = ctypes.CFieldAsDict(x)
            self.assertEqual(dict(d), {'a': 0})
            self.assertEqual(x.a, 0)
            d.a = 1
            self.assertEqual(dict(d), {'a': 1})
            self.assertEqual(x.a, 1)

        def test_c_field_unicode_fieldname(self):
            class X(ctypes.Structure):
                _fields_ = [(u'\xff', ctypes.c_int)]

            x = X()
            d =
