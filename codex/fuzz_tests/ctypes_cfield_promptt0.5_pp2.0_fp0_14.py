import ctypes
# Test ctypes.CField

import ctypes.test.test_cfield


class Test(ctypes.test.test_cfield.TestCase):
    def setUp(self):
        self.lib = ctypes.CDLL(self.lib_name)

    def tearDown(self):
        del self.lib

    def test_c_char_p(self):
        class X(ctypes.Structure):
            _fields_ = [("str", ctypes.c_char_p)]

        x = X()
        x.str = b"Hello"
        self.assertEqual(x.str, b"Hello")

        x.str = None
        self.assertEqual(x.str, None)

    def test_c_wchar_p(self):
        class X(ctypes.Structure):
            _fields_ = [("str", ctypes.c_wchar_p)]

        x = X()
        x.str = "Hello"
        self.assertEqual(x.str, "Hello")

        x.str = None
        self.assertEqual(
