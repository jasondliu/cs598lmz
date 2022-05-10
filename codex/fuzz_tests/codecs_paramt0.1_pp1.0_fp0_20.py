import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_utf8_to_utf16(self):
        self.assertEqual(
            codecs.utf_8_decode('\xed\xa0\x80\xed\xb0\x80', 'strict', True),
            (u'\ud800\udc00', 4)
        )
        self.assertEqual(
            codecs.utf_8_decode('\xed\xa0\x80\xed\xb0\x80', 'strict', False),
            (u'\ud800\udc00', 4)
        )
        self.assertEqual(
            codecs.utf_8_decode('\xed\xa0\x80\xed\xb0\x80', 'strict', None),
            (u'\ud800\udc00', 4)
        )
        self.assertEqual(
            codecs.utf_8_decode('\xed\xa0\x80
