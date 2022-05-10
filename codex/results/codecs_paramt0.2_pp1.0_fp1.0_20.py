import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test_codecs(unittest.TestCase):

    def test_bug_4489(self):
        # Test for bug 4489:  codecs.open() should not swallow
        # UnicodeDecodeErrors
        self.assertRaises(UnicodeDecodeError,
                          codecs.open, __file__, encoding="ascii")

    def test_bug_4561(self):
        # Test for bug 4561:  make sure that the BOM is not included
        # in the first line returned by readline()
        f = codecs.open(__file__, 'r', encoding='utf-16')
        self.assertEqual(f.readline(),
                         '#!/usr/bin/env python\n')

    def test_bug_4562(self):
        # Test for bug 4562:  make sure that the BOM is not included
        # in the first line returned by readline()
        f = codecs.open(__file__, 'r', encoding='
