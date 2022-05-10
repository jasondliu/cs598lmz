import codecs
# Test codecs.register_error

reload(codecs)

class Test_PEP293(unittest.TestCase):

    def test_bug1154902(self):
        teststr = u"\u3042\ufffd\u3044"
        x = codecs.getreader('iso2022_jp')(StringIO(teststr.encode('iso2022_jp')))
        y = codecs.getreader('iso2022_jp')(StringIO(teststr.encode('iso2022_jp')))
        self.assertEqual(next(x), u"\u3042")
        self.assertEqual(next(y), u"\u3042")

    def test_iso2022_jp(self):
        teststr = u"\u3042\ufffd\u3044"
        # First error handling (should not decode \x1b)
        x = codecs.getreader('iso2022_jp')(StringIO(teststr.encode('iso2022_jp')))
        self.assertRaises(UnicodeDecodeError,
