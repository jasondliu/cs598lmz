import codecs
# Test codecs.register_error()

import codecs
import unittest

from test import support

class CodecsModuleTestCase(unittest.TestCase):

    def test_encode(self):
        # Testing the 'strict' error handler
        self.assertEqual(codecs.encode("abc\u20ac", "latin-1", "strict"), b"abc\xe2\x82\xac")
        self.assertRaises(UnicodeEncodeError, codecs.encode, "\u20ac\u20ac", "latin-1", "strict")
        self.assertRaises(UnicodeEncodeError, codecs.encode, "abc\u20ac", "ascii", "strict")
        # Testing the 'ignore' error handler
        self.assertEqual(codecs.encode("abc\u20ac", "latin-1", "ignore"), b"abc")
        self.assertEqual(codecs.encode("\u20ac\u20ac", "latin-1", "ignore"), b"")
