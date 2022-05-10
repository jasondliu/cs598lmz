import codecs
# Test codecs.register_error()

import codecs
import io
import unittest
from test import support


class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test the register_error function.
        #
        # The test codec is a modified version of the 'ascii' codec.
        # The first step is to register it.
        codecs.register(lambda name: codecs.lookup('ascii') if name == 'test' else None)
        #
        # Encode a unicode string to bytes.
        # It will use the 'test' codec.
        # The 'test' codec will raise a UnicodeEncodeError.
        # The error handler will replace the character with '?'.
        s = 'a\u1234b'
        b = s.encode('test', 'replace')
        self.assertEqual(b, b'a?b')
        #
        # Decode bytes to a unicode string.
        # It will use the 'test' codec.
        # The 'test' codec will raise a UnicodeDec
