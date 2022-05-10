import codecs
codecs.register_error('testfail', lambda x: (u'', x.start + 1))

class Test(unittest.TestCase):

    def test_encode_error(self):
        arg = 'abc123'
        self.assertRaises(UnicodeEncodeError, codecs.escape_decode, arg, 'testfail')
        self.assertRaises(UnicodeEncodeError, codecs.escape_encode, arg, 'testfail')

    def test_decode_error(self):
        arg = 'abc123'
        self.assertRaises(UnicodeDecodeError, codecs.escape_decode, arg, 'testfail', 'strict')
        self.assertRaises(UnicodeDecodeError, codecs.escape_decode, arg, 'testfail', 'replace')
        self.assertRaises(UnicodeDecodeError, codecs.escape_decode, arg, 'testfail', 'ignore')

    def test_encode_decode(self):
        eq = self.assertEqual
        eq(codecs.escape_
