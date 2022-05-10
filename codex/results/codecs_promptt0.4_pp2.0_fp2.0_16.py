import codecs
# Test codecs.register_error()

import codecs
import unittest
import io

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Encoding
        encoder = codecs.getencoder('test.register_error')
        self.assertEqual(encoder('abc'), (b'abc', 3))
        self.assertEqual(encoder('\u3042'), (b'\xfe\xff\x30\x42', 2))
        self.assertRaises(UnicodeEncodeError, encoder, '\udc00')
        self.assertRaises(UnicodeEncodeError, encoder, '\udc00\u3042')
        self.assertEqual(encoder('\udc00\u3042', 'ignore'), (b'\x30\x42', 2))
        self.assertEqual(encoder('\udc00\u3042', 'replace'),
                         (b'\xfe\xff\x30\x42\x3f\x3f', 4))
        self
