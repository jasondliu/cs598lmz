import codecs
# Test codecs.register_error

# This test is here because the codecs module has a private
# _codecs_cn module, which is imported by the _multibytecodec
# module.  It is needed to test the ascii codec.

import test.test_support

# The codecs module is imported to ensure that the error
# handler is registered.
import codecs

import unittest

class TestAscii(unittest.TestCase):
    encoding = 'ascii'

    def test_decode(self):
        self.assertEqual(u"abc", "abc".decode(self.encoding))
        self.assertRaises(UnicodeDecodeError, "\x80".decode, self.encoding)
        self.assertRaises(UnicodeDecodeError, "\x80\x81".decode, self.encoding)
        self.assertRaises(UnicodeDecodeError, "\xc0\x80".decode, self.encoding)

    def test_encode(self):
        self.assertEqual("abc",
