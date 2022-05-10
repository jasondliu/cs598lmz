import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_utf8(unittest.TestCase):
    def test_utf8(self):
        self.assertEqual(u'\u00e9'.encode('utf-8'), b'\xc3\xa9')
        self.assertEqual(u'\u00e9'.encode('utf-8', 'strict'), b'\xc3\xa9')
        self.assertEqual(u'\u00e9'.encode('utf-8', 'ignore'), b'\xc3\xa9')
        self.assertEqual(u'\u00e9'.encode('utf-8', 'replace'), b'\xc3\xa9')
        self.assertEqual(u'\u00e9'.encode('utf-8', 'xmlcharrefreplace'), b'&#233;')
        self.assertEqual(u'\u00e9'.encode('utf-8', 'backslashreplace'), b'\\xe9')
        self.assertEqual(u'\
