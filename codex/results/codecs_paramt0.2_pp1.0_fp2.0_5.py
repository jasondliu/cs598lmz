import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test_codecs(unittest.TestCase):

    def test_bug_4489(self):
        # Test that the UTF-8 codec ignores BOM
        self.assertEqual(codecs.BOM_UTF8 + "abc",
                         codecs.utf_8_decode(codecs.BOM_UTF8 + "abc")[0])
        self.assertEqual(codecs.BOM_UTF8 + "abc",
                         codecs.utf_8_decode(codecs.BOM_UTF8 + "abc", "strict")[0])
        self.assertEqual(codecs.BOM_UTF8 + "abc",
                         codecs.utf_8_decode(codecs.BOM_UTF8 + "abc", "ignore")[0])

    def test_bug_1134692(self):
        # Test that the UTF-16 codecs accept BOM
        self.assertEqual(u"abc",
                         codecs.utf
