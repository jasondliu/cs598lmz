import codecs
codecs.register_error('strict', codecs.ignore_errors)


class Test(unittest.TestCase):

    def test_unicode_error(self):
        # Issue #18794: unicode(bytearray) should not raise UnicodeDecodeError
        # when the bytearray contains non-ASCII characters.
        self.assertEqual(unicode(bytearray(b'\xc3\xa9')), u'\xe9')
        self.assertEqual(unicode(bytearray(b'\xc3\xa9'), 'utf-8'), u'\xe9')
        self.assertEqual(unicode(bytearray(b'\xc3\xa9'), 'latin-1'), u'\xe9')
        self.assertEqual(unicode(bytearray(b'\xc3\xa9'), 'ascii', 'strict'),
                         u'\xe9')
        self.assertRaises(UnicodeDecodeError, unicode,
                          bytearray(b'\xc3\xa9'),
