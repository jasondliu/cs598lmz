import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test(unittest.TestCase):
    def test_utf8(self):
        self.assertEqual(b'\xc3\xa9'.decode('utf-8'), '\xe9')
        self.assertEqual(b'\xc3\xa9'.decode('utf-8', 'strict'), '\xe9')
        self.assertEqual(b'\xc3\xa9'.decode('utf-8', 'ignore'), '')
        self.assertEqual(b'\xc3\xa9'.decode('utf-8', 'replace'), '\ufffd')

    def test_utf8_surrogates(self):
        self.assertEqual(b'\xed\xa0\x80'.decode('utf-8', 'strict'), '\ud800')
        self.assertEqual(b'\xed\xa0\x80'.decode('utf-8', 'ignore'), '')
        self.assertEqual(b'\xed\xa0\x
