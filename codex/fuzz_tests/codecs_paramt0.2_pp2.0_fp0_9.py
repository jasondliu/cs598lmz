import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test_codecs(unittest.TestCase):

    def test_utf8(self):
        self.assertEqual(codecs.utf_8_decode(b'abc'), ('abc', 3))
        self.assertEqual(codecs.utf_8_decode(b'\xe4\xbd\xa0\xe5\xa5\xbd'),
                         ('\u4f60\u597d', 6))
        self.assertEqual(codecs.utf_8_decode(b'\xe4\xbd\xa0\xe5\xa5\xbd', 'strict'),
                         ('\u4f60\u597d', 6))
        self.assertEqual(codecs.utf_8_decode(b'\xe4\xbd\xa0\xe5\xa5\xbd', 'replace'),
                         ('\ufffd\u597d', 6))
        self.assertEqual(codecs.utf_8_
