import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_utf8_to_utf8(self):
        self.assertEqual(u'\u00A0',
                         utf8_decode(utf8_encode(u'\u00A0')))

    def test_utf8_to_utf8_with_invalid_bytes(self):
        self.assertEqual(u'\u00A0',
                         utf8_decode(utf8_encode(u'\u00A0\x80')))

    def test_utf8_to_utf8_with_invalid_bytes_strict(self):
        self.assertRaises(UnicodeDecodeError,
                          utf8_decode, utf8_encode(u'\u00A0\x80'),
                          'strict')

if __name__ == '__main__':
    unittest.main()
