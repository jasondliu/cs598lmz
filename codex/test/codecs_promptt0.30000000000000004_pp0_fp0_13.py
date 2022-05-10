import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Encoding
        def ignore_encoding_error(exc):
            if isinstance(exc, UnicodeEncodeError):
                return (u'', exc.end)
            raise TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.ignore_encoding", ignore_encoding_error)
        self.assertEqual(codecs.lookup_error("test.ignore_encoding"),
                         ignore_encoding_error)
        self.assertEqual(codecs.encode("abc\ud800", "ascii",
                                       "test.ignore_encoding"),
                         "abc")
        self.assertRaises(TypeError, codecs.encode, "abc\ud800", "ascii",
                          "test.ignore_encoding_error")

        # Decoding
