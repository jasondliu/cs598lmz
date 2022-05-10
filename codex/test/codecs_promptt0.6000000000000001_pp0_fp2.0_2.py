import codecs
# Test codecs.register_error()
# Test "surrogateescape" error handler

# This is the same as 'escape_encode_test.py' except that the error handler
# is set explicitly to "surrogateescape".

import codecs
import unittest
import sys

class TestSurrogates(unittest.TestCase):

    def test_surrogates(self):
        # Test \udcxx (0x010000 - 0x10ffff)
        # First test that the codec correctly decodes the surrogate pairs
        # (this is a pre-requisite for the test)
        for i in range(0xd800, 0xe000):
            u = chr(i) + chr(i+1)
            self.assertEqual(u.encode('utf-16-be'),
                             codecs.escape_decode(b'\\udc' + bytes([i>>8, i&0xff]))[0])
