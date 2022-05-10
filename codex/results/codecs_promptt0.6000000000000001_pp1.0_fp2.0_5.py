import codecs
# Test codecs.register_error and reader/writer

import test.support
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        self.assertRaises(LookupError, codecs.register_error, "undefined")
        self.assertRaises(TypeError, codecs.register_error, "strict", None)
        self.assertRaises(TypeError, codecs.register_error, "strict", "not callable")
        self.assertRaises(TypeError, codecs.register_error, "not callable", lambda x: x)

    def test_strict(self):
        u = "\u3042"
        s = b"\xa1\xa1"
        self.assertRaises(UnicodeError, u.encode, "iso-2022-jp", "strict")
        self.assertRaises(UnicodeError, u.encode, "iso-2022-jp", "strict")
        self.assertEqual(s.decode("utf-8", "strict"),
