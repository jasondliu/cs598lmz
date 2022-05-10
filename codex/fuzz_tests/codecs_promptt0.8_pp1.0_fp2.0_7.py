import codecs
# Test codecs.register_error('replace_with_space',replace_with_space)


class Test(unittest.TestCase):

    def test_decode(self):
        # Test default (strict) behaviour
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff')
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff\xff')
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff\xff\xff')
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff\xff\xff\xff')

        # Test the 'replace' error handler
        (s, size) = codecs.utf_8_decode(b'\xff', 'replace')
        self.assertEqual(s, '\ufffd')
        self.assertEqual(size, 1)

        (s, size) = codecs.utf_8_
