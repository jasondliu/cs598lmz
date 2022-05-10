import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test(unittest.TestCase):

    def test_utf8(self):
        self.assertEqual(
            codecs.decode(b'\x80', 'utf-8', 'strict'),
            '\ufffd')
        self.assertEqual(
            codecs.decode(b'\xc0\x80', 'utf-8', 'strict'),
            '\ufffd\ufffd')
        self.assertEqual(
            codecs.decode(b'\xc0\x80', 'utf-8', 'ignore'),
            '')
        self.assertEqual(
            codecs.decode(b'\xc0\x80', 'utf-8', 'replace'),
            '\ufffd\ufffd')
        self.assertEqual(
            codecs.decode(b'\xc0\x80', 'utf-8', 'xmlcharrefreplace'),
            '&#65533;&#65533;')
        self.assertE
