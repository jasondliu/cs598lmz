import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test_codecs(unittest.TestCase):

    def test_bug_4489(self):
        # Test for bug 4489:  codecs.open() should not swallow
        # UnicodeDecodeErrors
        self.assertRaises(UnicodeDecodeError,
                          codecs.open, TESTFN, "w", "ascii",
                          errors="strict")

    def test_bug_4564(self):
        # Test for bug 4564:  make sure that the BOM is the first
        # character when using utf-16
        f = codecs.open(TESTFN, "w", "utf-16")
        f.write("abc")
        f.close()
        f = open(TESTFN, "rb")
        s = f.read()
        f.close()
        self.assertEqual(s, '\xff\xfea\x00b\x00c\x00')

    def test_bug_5221(self):
