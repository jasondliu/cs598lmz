import codecs
# Test codecs.register_error()

import unittest
import codecs
import sys

class CodecRegistryTest(unittest.TestCase):
    def test_register_error(self):
        def handler(exc):
            if isinstance(exc, UnicodeDecodeError):
                return (u"\ufffd", exc.end)
            raise TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.codec", handler)

        # Encoding
        self.assertRaises(TypeError, codecs.register_error("test.codec", "foo"))

        # Decoding
        self.assertEqual("abc\ufffd".encode("ascii", "test.codec"), "abc\xfffd")

        codecs.register_error("test.codec", None)

def test_main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CodecRegistryTest))
    test_support.run_suite(suite)

if __name__ == "__
