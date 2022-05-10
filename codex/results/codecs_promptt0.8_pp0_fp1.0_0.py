import codecs
# Test codecs.register_error
import os
import sys
import tempfile
import types
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def unicode_error(*args):
            return ("Hello World", None)
        def unicode_error_handler(*args):
            return ("Goodbye World", None)
        codecs._register_error("unicode_error", unicode_error)
        codecs.register_error("unicode_error_handler", unicode_error_handler)
        self.assertRaises(UnicodeError, lambda: "Hello World".encode("unicode_error"))
        self.assertEqual(b"Goodbye World", "Hello World".encode("unicode_error_handler"))

class TestIgnore(unittest.TestCase):
    encoding = "utf_7"

    def test_ignore(self):
        s = b"abc\xffdef"
        u = s.decode(self.encoding, "ignore")
        self.assertEqual(u, "abcdef")
