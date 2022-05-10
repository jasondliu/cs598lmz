import codecs
codecs.register_error("strict", codecs.ignore_errors)

import unittest
class Test(unittest.TestCase):
    def test_replacement(self):
        self.assertEqual(b'abc\ufffd\ufffd\ufffd\u030a'.decode("ascii", "replace"), "abc???")
        self.assertEqual(b'abc\ufffd\ufffd\ufffd\u030a'.decode("latin-1", "replace"), "abc???")
        self.assertEqual(b'abc\x80\xff\x80\x30'.decode("latin-1", "replace"), "abc???0")

    def test_strict(self):
        self.assertRaises(UnicodeDecodeError, b'abc\ufffd\ufffd\ufffd\u030a'.decode, "ascii", "strict")
        self.assertRaises(UnicodeDecodeError, b'abc\ufffd\ufffd\ufffd\u030a'.decode, "latin-1", "strict
