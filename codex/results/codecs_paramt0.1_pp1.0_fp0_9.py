import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test_codecs(unittest.TestCase):

    def test_bug_4489(self):
        # Test for bug 4489:  codecs.open() should not swallow
        # UnicodeDecodeErrors
        self.assertRaises(UnicodeDecodeError,
                          codecs.open, TESTFN, 'w', 'ascii', 'strict')

    def test_bug_4564(self):
        # Test for bug 4564:  make sure that the BOM is the first
        # character when using UTF-16
        f = codecs.open(TESTFN, 'w', 'utf-16')
        f.write(u'\ufefftest')
        f.close()
        f = open(TESTFN, 'rb')
        data = f.read()
        f.close()
        self.assertEqual(data, '\xff\xfe\x00\x00\x00t\x00e\x00s\x00t\x00
