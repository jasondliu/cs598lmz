import codecs
# Test codecs.register_error()

import re
import unittest

from test import support


class TestRegisterError(unittest.TestCase):

    def test_simple(self):
        # Test simple codecs.register_error() usage
        def handler(exception):
            return ("?", exception.end)
        codecs.register_error("test.simple", handler)
        self.assertEqual("abc\ufffd\u0100\ufffd\ufffd".encode("ascii",
            "test.simple"), b"abc?\x01?")
        self.assertEqual("abc\ufffd\u0100\ufffd\ufffd".encode("ascii",
            "test.simple"), b"abc?\x01?")
        self.assertEqual("abc\ufffd\u0100\ufffd\ufffd".encode("ascii",
            "test.simple"), b"abc?\x01?")
        codecs.register_error("test.simple", None)
        self.assertEqual("abc\ufffd\u0100\ufffd\ufffd
