import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test_codecs(unittest.TestCase):

    def test_utf8_decode(self):
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n'), ('\xe9\n', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='strict'), ('\xe9\n', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='ignore'), ('\n', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='replace'), ('\ufffd\n', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='xmlcharrefreplace'), ('&#233;\n',
