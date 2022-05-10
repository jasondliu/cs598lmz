import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_utf8(unittest.TestCase):
    def test_utf8(self):
        self.assertEqual(u'\u00a0'.encode('utf8'), '\xc2\xa0')
        self.assertEqual(u'\u00a0'.encode('utf8', 'strict'), '\xc2\xa0')
        self.assertEqual(u'\u00a0'.encode('utf8', 'replace'), '\xc2\xa0')
        self.assertEqual(u'\u00a0'.encode('utf8', 'ignore'), '\xc2\xa0')
        self.assertEqual(u'\u00a0'.encode('utf8', 'xmlcharrefreplace'), '&#160;')
        self.assertEqual(u'\u00a0'.encode('utf8', 'backslashreplace'), '\\xa0')
        self.assertEqual(u'\u00a0'.encode('utf8', '
