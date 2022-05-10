import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(codecs.utf_8_decode('x'), ('x', 1))
        self.assertEqual(codecs.utf_8_decode('\x80'), ('\u0c00', 1))
        self.assertEqual(codecs.utf_8_decode('\xc0\x80'), ('\u0000', 2))
        self.assertEqual(codecs.utf_8_decode('\xc0\x80', 'strict'), ('\u0000', 2))
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, '\xc0\x80')
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, '\xc0\xc0')
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, '\xc0
