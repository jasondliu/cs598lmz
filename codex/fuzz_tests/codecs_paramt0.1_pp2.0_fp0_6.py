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
        # Test for bug 4564:  make sure that the BOM is not written
        # when encoding to UTF-16 or UTF-32
        for enc in ('utf-16', 'utf-16-le', 'utf-16-be',
                    'utf-32', 'utf-32-le', 'utf-32-be'):
            f = codecs.open(TESTFN, 'w', enc)
            f.write(u'\u20ac')
            f.close()
            f = open(TESTFN, 'rb')
            data = f.read()
