import codecs
# Test codecs.register_error

import codecs
import unittest
import test.test_support

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error
        def bad_decode(input, errors='strict'):
            raise UnicodeError, "bad decoding"
        def bad_encode(input, errors='strict'):
            raise UnicodeError, "bad encoding"
        codecs.register_error("test.bad", bad_decode)
        codecs.register_error("test.badencode", bad_encode)
        self.assertRaises(UnicodeError, unicode, "\xff", "ascii", "test.bad")
        self.assertRaises(UnicodeError, "abc".decode, "ascii", "test.bad")
        self.assertRaises(UnicodeError, "abc".decode, "ascii", "test.badencode")
        self.assertRaises(UnicodeError, u"\u1234".encode,
