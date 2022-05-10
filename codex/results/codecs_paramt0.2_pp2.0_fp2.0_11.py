import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_utf8_to_ascii(self):
        self.assertEqual(utf8_to_ascii('\xc3\xa9'), '\xe9')
        self.assertEqual(utf8_to_ascii('\xc3\xa9', 'strict'), '\xc3\xa9')
        self.assertEqual(utf8_to_ascii('\xc3\xa9', 'ignore'), '')
        self.assertEqual(utf8_to_ascii('\xc3\xa9', 'replace'), '?')
        self.assertEqual(utf8_to_ascii('\xc3\xa9', 'xmlcharrefreplace'), '&#233;')
        self.assertEqual(utf8_to_ascii('\xc3\xa9', 'backslashreplace'), '\\xc3\\xa9')
        self.assertEqual(utf8_to_ascii('\xc
