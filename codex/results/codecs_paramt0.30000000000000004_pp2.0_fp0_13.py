import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_utf8_to_utf16(self):
        self.assertEqual(
            codecs.utf_8_decode(b'\xC2\xA2', 'strict', True),
            (u'\u00A2', 2)
        )

        self.assertEqual(
            codecs.utf_8_decode(b'\xC2\xA2', 'strict', False),
            (u'\u00A2', 2)
        )

        self.assertEqual(
            codecs.utf_8_decode(b'\xC2\xA2', 'strict', None),
            (u'\u00A2', 2)
        )

    def test_utf8_to_utf16_surrogate(self):
        self.assertEqual(
            codecs.utf_8_decode(b'\xED\xA0\x80', 'strict', True),

