import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_latin1(unittest.TestCase):
    def test_latin1(self):
        # This is the Latin-1 encoding of the string 'Andr\xe9'.
        s = 'Andr\xe9'
        self.assertEqual(s.encode('latin-1'), b'Andr\xe9')
        self.assertEqual(s.encode('latin-1', 'strict'), b'Andr\xe9')
        self.assertEqual(s.encode('latin-1', 'ignore'), b'Andr')
        self.assertEqual(s.encode('latin-1', 'replace'), b'Andr?')
        self.assertEqual(s.encode('latin-1', 'xmlcharrefreplace'),
                         b'Andr&#233;')
        self.assertEqual(s.encode('latin-1', 'backslashreplace'),
                         b'Andr\\xe9')
        self.assertEqual(s
